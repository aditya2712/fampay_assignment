import requests
from datetime import datetime, timedelta

# import env vars from settings
from fampay_assignment.settings import YOUTUBE_API_KEY_1, YOUTUBE_API_KEY_2


def fetch_videos(tag: str, published_after: str):
    # published_before should be 1 day from today
    published_before = (datetime.utcnow() + timedelta(days=1)).isoformat("T") + "Z"
    API_KEY = YOUTUBE_API_KEY_2
    videos = []
    page_token = ""

    while 1:
        url = f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&q={tag}&type=video&order=date&publishedAfter={published_after}&publishedBefore={published_before}&key={API_KEY}&pageToken={page_token}"

        response = requests.get(url).json()

        if response.get("error"):
            print("Error:", response["error"]["message"])
            return videos

        for item in response["items"]:
            video = {}
            video["id"] = item["id"]["videoId"]
            video["title"] = item["snippet"]["title"]
            video["description"] = item["snippet"]["description"]
            video["published_at"] = item["snippet"]["publishedAt"]
            video["channel_title"] = item["snippet"]["channelTitle"]

            video["thumbnail_urls"] = []
            for thumbnail in item["snippet"]["thumbnails"].values():
                video["thumbnail_urls"].append(thumbnail["url"])

            videos.append(video)

        if "nextPageToken" in response:
            page_token = response["nextPageToken"]
            # TODO: Remove this break in production, its just for testing to reduce quota
            break
        else:
            break

    return videos
