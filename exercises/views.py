from django.shortcuts import render, get_object_or_404
from .models import Exercise

def Exercises(request):
  all_exercises = Exercise.objects.all()

  return render(request, 'teacher/exercises.html', {'exercises':all_exercises})

def NewExercise(request):
  return