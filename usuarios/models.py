from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Usuario(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('password',)