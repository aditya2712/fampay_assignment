# Generated by Django 4.1.5 on 2023-01-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("youtube", "0002_rename_tags_video_tag"),
    ]

    operations = [
        migrations.RenameField(
            model_name="video",
            old_name="videoId",
            new_name="video_id",
        ),
        migrations.RemoveField(
            model_name="video",
            name="urls",
        ),
        migrations.AddField(
            model_name="tag",
            name="last_fetched_at",
            field=models.CharField(default="default", max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="video",
            name="channel_title",
            field=models.CharField(default="default", max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="video",
            name="thumbnail_url",
            field=models.CharField(default="default", max_length=200),
            preserve_default=False,
        ),
    ]