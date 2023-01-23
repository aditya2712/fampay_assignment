from django.db import models
from django.contrib.postgres.fields import ArrayField


class Video(models.Model):
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE, blank=False, null=False)

    title = models.CharField(max_length=200, blank=False, null=False)
    published_date = models.DateTimeField("date published", blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    video_id = models.CharField(max_length=200, blank=False, null=False)
    thumbnail_url = models.CharField(max_length=200, blank=False, null=False)
    channel_title = models.CharField(max_length=200, blank=False, null=False)


class Tag(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    last_fetched_at = models.CharField(max_length=200, blank=True, null=True)