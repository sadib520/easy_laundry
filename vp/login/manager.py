from django.contrib.auth.models import BaseUserManager



class custom_usermanager(BaseUserManager):

    def create_user(self, email, password, name=None, number=None): 
#* email, password is a required parameter. If a caller does not provide it, Python will raise an error. name, and number are optional parameters because they have default values set to None

        if not email:
            raise ValueError('Email must be provided.')
        elif not password:
            raise ValueError('Password must be provided')
        
        email = self.normalize_email(email) #* xyz@gmail.com and XYZ@gmail.com both are same
        user = self.model(email=email, name=name, number=number)
        user.set_password(password)
        user.save(using=self._db)

        return user

