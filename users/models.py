from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser,PermissionsMixin):
    
    email = models.EmailField(unique=True)
    name=models.CharField('Nombre',max_length= 100)
    last_name=models.CharField('Apellido',max_length=100)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_name(self):
        return self.name

