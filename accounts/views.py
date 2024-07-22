from django.shortcuts import render, redirect, get_object_or_404
from .forms import SchoolUserCreationForm, LoginForm
from .models import SchoolUser 
from dashboard.models import EnrolledStudent, Teacher
from dashboard.forms import StudentDataForm, TeacherDataForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from dashboard.views import manager_required
from django.contrib import messages

def Login(request):
  form = LoginForm()
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        if user.role == 'Student':
          return redirect('dashboard:Student_Home')
        elif user.role == 'Teacher':
          return redirect('dashboard:Teacher_Home')
        elif user.role == 'Manager':
          return redirect('dashboard:Manager_Home')
  return render(request, 'login.html', {'form':form})

@login_required
@manager_required
def RegisterUser(request):
  if request.user.is_staff:
    if request.method == 'POST':
      form = SchoolUserCreationForm(request.POST)
      if form.is_valid():
        user = form.save()
        if user.role == 'Student':
          return redirect('Add_Student_Data', user.id)
        elif user.role == 'Teacher':
          return redirect('Add_Teacher_Data', user.id)
    else:
      form = SchoolUserCreationForm()

    return render(request, 'register.html', {'form':form})

def AddStudentData(request, id):
  user = get_object_or_404(SchoolUser, id=id)
  if request.method == 'POST':
    student_form = StudentDataForm(request.POST)
    if student_form.is_valid():
      new_student = EnrolledStudent.objects.create(
          user = user,
          major = student_form.cleaned_data['major'],
          student_id = student_form.cleaned_data['student_id']
      )
      new_student.save()
      return redirect('Manage_Users')
    return render(request, 'userDataRegister/add_user_data.html', {'user':user,
                                                                  'student_form':student_form})
  return render(request, 'userDataRegister/user_data.html', {'user':user})

def AddTeacherData(request, id):
  user = get_object_or_404(SchoolUser, id=id)
  if request.method == 'POST':
    teacher_form = TeacherDataForm(request.POST)
    if teacher_form.is_valid():
      new_teacher = Teacher.objects.create(
        user = user,
        teacher_id = teacher_form.cleaned_data['teacher_id'],
        occupation = teacher_form.cleaned_data['occupation']
      )
      new_teacher.save()
      return redirect('Manage_Users')
    return render(request, 'userDataRegister/add_user_data.html', {'user':user,
                                                                  'teacher_form':teacher_form})
  return render(request, 'userDataRegister/user_data.html', {'user':user})

def Logout(request):
  logout(request)
  return redirect('Login')
