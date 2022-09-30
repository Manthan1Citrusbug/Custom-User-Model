from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not name:
            raise ValueError("User must have a full name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.name = name
        user.set_password(password)  # change password to hash
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user

class UserModel(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(unique=True,max_length=100)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    create_date = models.DateTimeField(default = datetime.today())
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD =  'email'
    REQUIRED_FIELDS =  []
    objects = UserManager()
    
    def __str__(self):
        return self.email

    
