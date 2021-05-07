from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(max_length=200)
    phone = PhoneNumberField()