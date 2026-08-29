from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import UserModel, UserProfile 



@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance,
            phone=instance.phone,  
            id_code=instance.id_code  
        )