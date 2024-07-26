from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from functools import wraps

def manager_required(view_func):
  @wraps(view_func)
  def _wrapped_view(request, *args, **kwargs):
    if request.user.is_authenticated and request.user.role == 'Manager':
        return view_func(request, *args, **kwargs)
    return redirect('Login')
  return _wrapped_view

def student_required(view_func):
  @wraps(view_func)
  def _wrapped_view(request, *args, **kwargs):
    if request.user.is_authenticated and request.user.role == 'Student':
        return view_func(request, *args, **kwargs)
    return redirect('Login')
  return _wrapped_view

def teacher_required(view_func):
  @wraps(view_func)
  def _wrapped_view(request, *args, **kwargs):
    if request.user.is_authenticated and request.user.role == 'Teacher':
        return view_func(request, *args, **kwargs)
    return redirect('Login')
  return _wrapped_view

@login_required
@manager_required
def ManagerHome(request):
  return render(request, 'manager/home.html')

@login_required
@student_required
def StudentHome(request):
  return render(request, 'student/home.html')

@login_required
@teacher_required
def TeacherHome(request):
  return render(request, 'teacher/home.html')




    
