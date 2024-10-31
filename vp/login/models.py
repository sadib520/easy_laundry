from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(("Email Address"), max_length=30)
    password1 = models.CharField(max_length=16)
    password2 = models.CharField(max_length=128, null=True, blank=True)
