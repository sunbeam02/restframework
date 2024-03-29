from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    address= models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.user.first_name