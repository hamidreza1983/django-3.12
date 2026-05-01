from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserModel, Profile

# this signal runs after a UserModel instance is saved
@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    # if the user is newly created, automatically create a profile for them
    if created:
        Profile.objects.create(user=instance)
