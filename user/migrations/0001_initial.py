# Generated by Django 4.1 on 2022-08-04 17:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.EmailField(blank=True, max_length=250, null=True)),
                ("intro", models.CharField(blank=True, max_length=200, null=True)),
                ("bio", models.TextField(blank=True, null=True)),
                ("steam", models.CharField(blank=True, max_length=300, null=True)),
                ("twitch", models.CharField(blank=True, max_length=300, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
