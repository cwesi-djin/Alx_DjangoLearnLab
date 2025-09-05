from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(models.Model):
    bio = models.TextField()
    profile_picture = models.ImageField(blank=True, null=True)
    followers = models.ManyToManyField("self", symmetrical=False, blank=True, related_name='following')