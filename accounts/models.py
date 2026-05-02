from django.db import models
import uuid
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



#class CustomUserModel(AbstractUser):
#    id_code = models.CharField(max_length=10, blank=True)
#    phone = models.CharField(max_length=12, blank=True)


class CustomeManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            return ValueError("email can not be empty...!")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("is_active", True)
        #kwargs.setdefault("is_abbas", True)
        if kwargs.get("is_staff") is not True:
            raise ValueError("is_staff for superuser vajebeh")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("is_superuser for superuser vajebeh")
        if kwargs.get("is_active") is not True:
            raise ValueError("is_active for superuser vajebeh")
        #if kwargs.get("is_abbas") is not True:
            #raise ValueError("is_abbas for superuser vajebeh")
        return self.create_user(email, password, **kwargs)
        
class UserModel(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    #id_code = models.CharField(max_length=10, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    #is_abbas = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    objects = CustomeManager()

    def __str__(self):
        return self.email
    

def validate_phone(value):
    if not value.isdigit() or len(value) != 11:
        raise ValueError('The phone number must be 11 digits long and numeric.')

def validate_codmeli(value):
    if not value.isdigit() or len(value) != 10:
        raise ValueError('The codmeli number must be 11 digits long and numeric.')



def phon_uuid():
    return str(uuid.uuid4())[:11]

def codmeli_uuid():
    return str(uuid.uuid4())[:10]


class UserProfile(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, unique=True,validators=[validate_phone], default=phon_uuid)
    id_code = models.CharField(max_length=10, unique=True,validators=[validate_codmeli], default=codmeli_uuid)
    image = models.ImageField(upload_to="profile/", null=True, blank=True)
