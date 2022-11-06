from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User

#@receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created == True:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name + " " + user.last_name
        )

#@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)