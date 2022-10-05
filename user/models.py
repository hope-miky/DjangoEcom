from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser as AbstractBaseUser

# Create your models here.

class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given phonenumber must be set')
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomerManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)


class Customer(AbstractBaseUser):
    email  = models.EmailField(unique=True, max_length=30)
    username = models.CharField(unique=True, max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomerManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'



class CustomerDetails(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    dbo = models.DateTimeField()
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE)



class User(AbstractUser):
    
    email  = models.EmailField(unique=True, max_length=100)
    phone_number = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


    


