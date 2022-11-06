from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, default="default_profile.jpg")
    steam = models.CharField(max_length=300, blank=True, null=True)
    twitch = models.CharField(max_length=300, blank=True, null=True)
    discord = models.CharField(max_length=300, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)

class CompRank(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    game_name = models.CharField(max_length=100, blank=True, null=True)
    rank = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.owner.name}:{self.game_name}:{self.rank}"