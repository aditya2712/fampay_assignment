# Generated by Django 4.1.5 on 2023-01-23 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("youtube", "0003_rename_videoid_video_video_id_remove_video_urls_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="last_fetched_at",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
