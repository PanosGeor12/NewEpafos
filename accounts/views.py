from django.shortcuts import render, redirect, get_object_or_404
from .forms import SchoolUserCreationForm, LoginForm
from .models import SchoolUser 
from .models import EnrolledStudent, Teacher
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from dashboard.views import manager_required

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
    student_form = forms.StudentDataForm(request.POST)
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
    teacher_form = forms.TeacherDataForm(request.POST)
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
  return redirect('accounts:Login')

@login_required
@manager_required
def ManageUsers(request):
  all_users = SchoolUser.objects.all()
  roles = SchoolUser.objects.values_list('role', flat=True).distinct()
  selected_role = request.GET.get('role', 'all')

  if selected_role != 'all':
    users = SchoolUser.objects.filter(role=selected_role)
  else:
    users = all_users

  return render(request, 'manageusers/users.html', {
                                                'roles':roles,
                                                'users':users,
                                                'selected_role':selected_role})

def UserDetails(request, id):
  user = get_object_or_404(SchoolUser, id=id)
  return render(request, 'manageusers/details.html', {'user':user})

@login_required
@manager_required
def EditUser(request, id):
  user = get_object_or_404(SchoolUser, id=id)
  teacher = Teacher.objects.get(user=user)if user.role == 'Teacher' else None
  student = EnrolledStudent.objects.get(user=user)if user.role == 'Student' else None
  if request.method == 'POST':
    form = forms.EditSchoolUser(request.POST, instance=user)
    teacher_data = forms.EditTeacherData(request.POST, instance=teacher)if user.role == 'Teacher' else None
    student_data = forms.EditStudentData(request.POST, instance=student)if user.role == 'Student' else None
    if user.role == 'Student':
      if form.is_valid() and student_data.is_valid():
          form.save()
          student_data.save()
          return redirect('User_Details', user.id)
    elif user.role == 'Teacher':
      if form.is_valid() and teacher_data.is_valid():
          form.save()
          teacher_data.save()
          return redirect('User_Details', user.id)
  else:
    form = forms.EditSchoolUser(instance=user)
    teacher_data = forms.EditTeacherData(instance=teacher)if user.role == 'Teacher' else None
    student_data = forms.EditStudentData(instance=student)if user.role == 'Student' else None
    
  return render(request, 'manageusers/edituser.html', {'form':form,
                                                  'student_data':student_data,
                                                  'teacher_data':teacher_data, 
                                                  'user':user})
@manager_required
def DeleteUser(request, id):
  user = SchoolUser.objects.get(id=id)
  if request.method == 'POST':
      user.delete()
      return redirect('Manage_Users')
  
  return render(request, 'manageusers/deleteuser.html',{'user':user})

