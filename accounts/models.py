from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser



class CustomUserModel(AbstractUser):
    id_code = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=12, blank=True)