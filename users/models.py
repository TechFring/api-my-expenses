from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    salary = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    password = models.CharField(max_length=128, blank=True)
    email = models.EmailField(unique=True)
    photo_url = models.CharField(max_length=255, blank=True)
