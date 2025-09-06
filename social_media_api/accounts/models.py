from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=128, unique=True,blank=True)
    bio = models.TextField()
    profile_picture = models.ImageField(blank=True, null=True)
    password = models.CharField(max_length=128, blank=True)
    followers = models.ManyToManyField("self", symmetrical=False, blank=True, related_name='following')

    def __str__(self):
        return self.username