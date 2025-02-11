from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mail = models.EmailField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=False)
    profile_picture = models.ImageField(null=True, blank=True)
    address = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.username

# Create your models here.
