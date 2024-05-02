from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=10, unique=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username']
    


