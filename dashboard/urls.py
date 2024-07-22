from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('manager/', views.ManagerHome, name='Manager_Home'),
    path('student/', views.StudentHome, name='Student_Home'),
    path('teacher/', views.TeacherHome, name='Teacher_Home'),
    path('manager/manageusers/', views.ManageUsers, name='Manage_Users'),
    path('manager/manageuser/<int:id>', views.UserDetails, name='User_Details'),
    path('manager/edituser/<int:id>', views.EditUser, name='Edit_User'),
    path('manager/deleteuser/<int:id>', views.DeleteUser, name='Delete_User'),
    path('manager/manageposts/', views.ManagePosts, name='Manage_Posts'),
    path('student/schoolnews/', views.SchoolPosts, name='School_News'),
]
