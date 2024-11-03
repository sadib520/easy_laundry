from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .manager import custom_usermanager
# Create your models here.
class custom_user(AbstractBaseUser, PermissionsMixin):  #! models.Model etar mane amra django default model use korchi. user mane ekhane custom user model create kora hoice.
    name = models.CharField(max_length=25)
    email = models.EmailField(("Email Address"), max_length=30, unique=True)
    number = models.IntegerField(("number"),)
    password = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True) 
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = custom_usermanager() #! By defining objects = CustomUserManager(), you're overriding the default manager for your custom user model with your CustomUserManager instance.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'number']



#* This field indicates whether the user account is active. It's often used to "deactivate" an account without actually deleting it from the database.

#* A custom model also requires some additional properties, such as
#* USERNAME_FIELD — This is a string describing the unique identifier; in our case, its email.
#* REQUIRED_FIELDS - a list of mandatory fields required when creating a new user. Add the properties to the User model.

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin





