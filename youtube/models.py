from django.db import models
from django.contrib.postgres.fields import ArrayField


class Video(models.Model):
    tags = models.ForeignKey("Tag", on_delete=models.CASCADE, blank=False, null=False)

    title = models.CharField(max_length=200, blank=False, null=False)
    published_date = models.DateTimeField("date published", blank=False, null=False)
    urls = models.URLField(blank=False, null=False)
    thumbnail_urls = ArrayField(models.URLField(), blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    videoId = models.CharField(max_length=200, blank=False, null=False)


class Tag(models.model):
    name = models.CharField(max_length=200, blank=False, null=False)
