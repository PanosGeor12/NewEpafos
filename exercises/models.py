from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from accounts.models import Major
from accounts.models import SchoolUser

class Exercise(models.Model):
  name = models.CharField(max_length=255)
  description = CKEditor5Field(config_name='extends')
  slug = models.SlugField(max_length=255)
  for_major = models.ForeignKey(Major,
                                on_delete=models.CASCADE)
  for_students = models.ManyToManyField(SchoolUser, limit_choices_to={'role':'Student'})
  uploaded_files = models.FileField(upload_to='exercises/')
  uploaded = models.DateTimeField(auto_now=True)
  deadline = models.DateTimeField(auto_created=False)

  def __str__(self):
    return f'{self.name} - {self.uploaded.date()}'

class SubmittedExercise(models.Model):
  class Status(models.TextChoices):
    DRAFT = 'Draft', 'Draft'
    PUBLISHED = 'Published', 'Published'
  student = models.OneToOneField(SchoolUser, on_delete=models.CASCADE)
  exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
  student_answer = models.FileField(upload_to='submitted/', null=True, blank=True)
  typed_answer = models.TextField(null=True, blank=True)
  status = models.CharField(max_length=10,
                            choices=Status.choices,
                            default=Status.DRAFT)
  submitted_at = models.DateTimeField(null=True)

  def __str__(self):
    return f'{self.student} - {self.exercise}'

  