from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
# "sample_app" is name of the root app
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fampay_assignment.settings")

app = Celery(
    "celery_app", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "fetch_youtube_videos_task": {
        "task": "youtube.tasks.fetch_youtube_videos",
        "schedule": 10,
    },
}
