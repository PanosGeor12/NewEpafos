from django.shortcuts import render, get_object_or_404, redirect
from .models import Exercise
from .forms import AddNewExercise
from dashboard.views import teacher_required,student_required

@teacher_required
def AllExercises(request):
  all_exercises = Exercise.objects.all()

  return render(request, 'teacher/exercises.html', {'exercises':all_exercises})

@teacher_required
def NewExercise(request):
  if request.method == 'POST':
    exercise_form = AddNewExercise(request.POST)
    if exercise_form.is_valid():
      exercise_form.save()
      return redirect('exercises:Teacher_Exercises')
  else:
    exercise_form = AddNewExercise()
  return render(request, 'teacher/add_exercise.html', {'exercise_form':exercise_form})