from django.urls import path
from . import views

app_name = 'exercises'

urlpatterns = [
  path('teacher/exercises', views.AllExercises, name='Teacher_Exercises'),
  path('teacher/addexercise', views.NewExercise, name='Add_New_Exercise'),
]
