from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# specifies what happens after a new instance of a model is created
  # in this case, on user profile save, a new profile is created as well

# a decorator that specifies 
# at which signal and sender the receiver gets fired
@receiver(post_save, sender=User)
# **kwargs allows the function to accept some additional arguments
def create_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)
  
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()