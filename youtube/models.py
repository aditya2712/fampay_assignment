from django.db import models
from django.contrib.postgres.fields import ArrayField


class Video(models.Model):
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE, blank=False, null=False)

    title = models.CharField(max_length=200, blank=False, null=False)
    published_date = models.DateTimeField("date published", blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    videoId = models.CharField(max_length=200, blank=False, null=False)


class Tag(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
