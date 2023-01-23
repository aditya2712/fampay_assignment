from datetime import datetime

from .utils import fetch_videos
from .constants import DEFAULT_PUBLISHED_AFTER
from .models import Tag, Video
from fampay_assignment.celery import app

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)



# Periodic task for fetching youtube videos
@app.task
def fetch_youtube_videos():
    # fetch all tags
    tags = Tag.objects.all()
    for tag in tags:
        # fetch all videos for this tag
        last_fetched_at = (
            tag.last_fetched_at if tag.last_fetched_at else DEFAULT_PUBLISHED_AFTER
        )
        videos = fetch_videos(tag=tag.name, published_after=last_fetched_at)
        for video in videos:
            # check if video already exists
            if not Video.objects.filter(video_id=video["id"]).exists():
                # create video
                Video.objects.create(
                    video_id=video["id"],
                    title=video["title"],
                    description=video["description"],
                    published_date=video["published_at"],
                    thumbnail_url=video["thumbnail_urls"][0],
                    channel_title=video["channel_title"],
                    tag=tag,
                )
        # update last_fetched_at for this tag
        tag.last_fetched_at = datetime.utcnow().isoformat("T") + "Z"
        tag.save()
