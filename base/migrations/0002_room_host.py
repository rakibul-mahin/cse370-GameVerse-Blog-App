# Generated by Django 4.1 on 2022-08-04 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_profile_username"),
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="host",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user.profile",
            ),
        ),
    ]
