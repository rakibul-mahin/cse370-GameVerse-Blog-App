# Generated by Django 4.1 on 2022-08-22 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_alter_message_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="topic",
            name="dveloper",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
