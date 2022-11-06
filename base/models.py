from django.db import models
from user.models import Profile
import uuid

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=160)
    dveloper = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    host = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(Profile, related_name='participants', blank=True)
    image = models.ImageField(null=True, blank=True, default="default_room.jpg")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created'] #- will be in descending order (latest)

    def __str__(self):
        return self.title

class Message(models.Model):
    user = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[:50]

class Item(models.Model):
    creator = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    sold = models.BooleanField(default=False, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    gamername = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(default=0, null=True, blank=True)
    accountlevel = models.IntegerField(default=0, null=True, blank=True)
    buyer = models.CharField(max_length=100, default="No Buyer")

    def __str__(self):
        return (f"{self.creator}:{self.gamername}")
