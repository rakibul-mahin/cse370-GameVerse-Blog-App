# Generated by Django 4.1 on 2022-08-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0006_topic_dveloper"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="image",
            field=models.ImageField(
                blank=True, default="default_room.jfif", null=True, upload_to=""
            ),
        ),
    ]
