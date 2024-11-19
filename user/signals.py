from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

# This is to signal to the profiles database when a new user creates an account from the front end
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwarks):
    if created:
        Profile.objects.create(student=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwarks):
    instance.profile.save()
