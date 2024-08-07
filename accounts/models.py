from django.db import models
from django.contrib.auth.models import AbstractUser
from dashboard.models import Major

class SchoolUser(AbstractUser):
  id = models.AutoField(primary_key=True)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  birthdate = models.DateField(blank=True, auto_now_add=False, null=True)
  role = models.CharField(max_length=20, choices={'Teacher':'Teacher', 'Student':'Student', 'Manager':'Manager'})
  phone_number = models.CharField(max_length=10)
  address = models.CharField(max_length=100, null=True)

class EnrolledStudent(models.Model):
  def get_majors():
    return [(major.name , major.name) for major in Major.objects.all()]
  student_id = models.CharField(max_length=4, primary_key=True)
  user = models.OneToOneField(SchoolUser, on_delete=models.CASCADE)
  major = models.ForeignKey(Major, on_delete=models.CASCADE)
  def __str__(self):
    return self.student_id

class Teacher(models.Model):
  teacher_id = models.CharField(max_length=10, primary_key=True)
  user = models.OneToOneField(SchoolUser, on_delete=models.CASCADE)
  occupation = models.CharField(max_length=100)
  def __str__(self):
    return self.teacher_id