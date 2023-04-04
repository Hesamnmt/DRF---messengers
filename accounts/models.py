from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManger


class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=11)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    info = models.CharField(max_length=300)

    object = UserManger()
    USERNAME_FIELDS = ['phone_number']


    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.phone_number}'

