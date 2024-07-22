from django.db import models
from django.utils import timezone
from accounts.models import SchoolUser
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse

class Post(models.Model):
  class Categories(models.TextChoices):
    STUDENTSHIP = 'Studentship', 'Studentship'
    EOPEP = 'EOPEP', 'Eopep Examinations'
    EXAMINATIONS = 'EXAMS', 'Examinations'
  
  class Status(models.TextChoices):
    DRAFT = 'Draft', 'Draft'
    PUBLISHED = 'Published', 'Published'

  title = models.CharField(max_length=255)
  category = models.CharField(max_length=15,
                              choices=Categories.choices,
                              default=Categories.STUDENTSHIP)
  slug = models.SlugField(max_length=255, unique_for_date='published')
  author = models.ForeignKey(SchoolUser,
                            on_delete=models.CASCADE,
                            related_name='news')
  body = CKEditor5Field(config_name='extends')
  published = models.DateTimeField(default=timezone.now)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=10,
                            choices=Status.choices,
                            default=Status.DRAFT)

  class Meta:
    ordering = ['-published']
    indexes = [ 
          models.Index(fields=['-published']),
        ]
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse('core:Post_Details', args=[self.published.year,
                                              self.published.month,
                                              self.published.day,
                                              self.slug])
  def news_get_absolute_url(self):
      return reverse('news:Post_Details', args=[self.published.year,
                                                self.published.month,
                                                self.published.day,
                                                self.slug])
  def manager_get_absolute_url(self):
      return reverse('news:Manager_Post_Details', args=[self.published.year,
                                                self.published.month,
                                                self.published.day,
                                                self.slug])
  