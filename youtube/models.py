from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    published_date = models.DateTimeField("date published", blank=False, null=False)
    url = models.URLField(blank=False, null=False)
    thumbnail_url = models.URLField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
