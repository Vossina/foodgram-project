from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length = 50,blank=True, null=True, unique = True)
    email = models.EmailField(unique = True)
    # first_name = models.CharField(max_length = 50)
    # last_name = models.CharField(max_length = 50)
    # is_subscribed = models.BooleanField()
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username
