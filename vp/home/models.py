from django.db import models
from django.utils import timezone

class contact_model(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=15)  # Store phone numbers as CharField
    email = models.CharField(max_length=30)
    msg = models.CharField(max_length=300)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name  # This will display the contact's name in Django admin
