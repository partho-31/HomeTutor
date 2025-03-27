from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager


class User(AbstractUser):
    Teacher = 'Teacher'
    Student = 'Student'
    STATUS_CHOICES = [
        (Teacher,'Teacher'),
        (Student,'Student')
    ]

    username = None
    email = models.EmailField( unique= True)
    address = models.CharField(max_length= 200, blank= True, null= True)
    phone_number = models.CharField(max_length= 15, blank= True, null= True)
    role = models.CharField(max_length=8, choices= STATUS_CHOICES, default= 'Student')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.get_full_name()
    
