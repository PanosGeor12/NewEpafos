from django.db import models
from django.contrib.auth.models import AbstractUser

class SchoolUser(AbstractUser):
  id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  birthdate = models.DateField(blank=True, auto_now_add=False, null=True)
  age = models.CharField(blank=True, max_length=2, null= True)
  role = models.CharField(max_length=20, choices={'Teacher':'Teacher', 'Student':'Student', 'Manager':'Manager'})
  phone_number = models.CharField(max_length=10)
  address = models.CharField(max_length=100, null=True)
  