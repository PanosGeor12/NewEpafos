from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import SchoolUser
from .models import EnrolledStudent, Teacher
from .forms import EditStudentData, EditSchoolUser, EditTeacherData
from news.models import Post
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

  return render(request, 'manager/users/users.html', {
                                                'roles':roles,
                                                'users':users,
                                                'selected_role':selected_role})

def UserDetails(request, id):
  user = get_object_or_404(SchoolUser, id=id)
  return render(request, 'manager/users/details.html', {'user':user})

@login_required
@manager_required
def EditUser(request, id):
  user = get_object_or_404(SchoolUser, id=id)
  teacher = Teacher.objects.get(user=user)if user.role == 'Teacher' else None
  student = EnrolledStudent.objects.get(user=user)if user.role == 'Student' else None
  if request.method == 'POST':
    form = EditSchoolUser(request.POST, instance=user)
    teacher_data = EditTeacherData(request.POST, instance=teacher)if user.role == 'Teacher' else None
    student_data = EditStudentData(request.POST, instance=student)if user.role == 'Student' else None
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
    form = EditSchoolUser(instance=user)
    teacher_data = EditTeacherData(instance=teacher)if user.role == 'Teacher' else None
    student_data = EditStudentData(instance=student)if user.role == 'Student' else None
    
  return render(request, 'manager/users/edituser.html', {'form':form,
                                                  'student_data':student_data,
                                                  'teacher_data':teacher_data, 
                                                  'user':user})
@manager_required
def DeleteUser(request, id):
  user = SchoolUser.objects.get(id=id)
  if request.method == 'POST':
      user.delete()
      return redirect('Manage_Users')
  
  return render(request, 'manager/users/deleteuser.html',{'user':user})

@manager_required
def ManagePosts(request):
  all_posts = Post.objects.all()
  categories = Post.Categories.choices
  selected_category = request.GET.get('category', 'all')
  
  if selected_category != 'all':
    posts = Post.objects.filter(category=selected_category)
  
  else:
    posts = all_posts
  return render(request, 'manager/news/manageposts.html', {'posts':posts, 
                                                           'categories':categories})

@login_required
def SchoolPosts(request):
  posts = Post.objects.filter(status=Post.Status.PUBLISHED)
  
  if request.user.role == 'Teacher':
    return render(request, 'schoolnews/teachernews.html',{'posts':posts})
  elif request.user.role == 'Student':
    return render(request, 'schoolnews/studentnews.html',{'posts':posts})

    
