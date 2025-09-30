from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
import uuid
from .manager import UserManager

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('teacher','Учитель'),
        ('student','Студент'),
    )
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=300, blank=True)
    role  = models.CharField(max_length=15, choices=ROLE_CHOICES,default='student')

    objects = UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []

    def create_activation_code(self):
        code = str(uuid.uuid4())
        self.activation_code = code
        self.save()
