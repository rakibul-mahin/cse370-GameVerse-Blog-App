# Generated by Django 4.1 on 2022-08-05 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_profile_discord_comprank"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                blank=True, default="default_profile.jpg", null=True, upload_to=""
            ),
        ),
    ]