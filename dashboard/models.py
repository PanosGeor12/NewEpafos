from django.db import models
from accounts.models import SchoolUser

class Major(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  def __str__(self):
    return self.name

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