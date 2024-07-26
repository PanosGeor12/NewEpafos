from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterUser, name='Register_User'),
    path('addstudentdata/<int:id>', views.AddStudentData, name='Add_Student_Data'),
    path('addteacherdata/<int:id>', views.AddTeacherData, name='Add_Teacher_Data'),
    path('login/', views.Login, name='Login'),
    path('logout/', views.Logout, name='Logout'),
    path('manager/manageusers/', views.ManageUsers, name='Manage_Users'),
    path('manager/manageuser/<int:id>', views.UserDetails, name='User_Details'),
    path('manager/edituser/<int:id>', views.EditUser, name='Edit_User'),
    path('manager/deleteuser/<int:id>', views.DeleteUser, name='Delete_User'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
