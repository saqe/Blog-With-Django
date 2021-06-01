from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


# When you receive a signal of user is saved, then create a profile
@receiver(post_save, sender=User)
def create_profile(sender,instance,created, **kwargs):
    # If user is created, create a profile
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()
