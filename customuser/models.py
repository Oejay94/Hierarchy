from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True, blank=True)
    first_name = models.CharField(max_length=50)

    def __str__(self):
        return self.username