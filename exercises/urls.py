from django.urls import path
from . import views

app_name = 'exercises'

urlpatterns = [
  path('teacher/exercises', views.Exercises, name='Teacher_Exercises')
]
