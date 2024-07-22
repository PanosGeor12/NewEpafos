from django.urls import path
from .views import RegisterUser, Login ,Logout, AddStudentData, AddTeacherData
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', RegisterUser, name='Register_User'),
    path('addstudentdata/<int:id>', AddStudentData, name='Add_Student_Data'),
    path('addteacherdata/<int:id>', AddTeacherData, name='Add_Teacher_Data'),
    path('login/', Login, name='Login'),
    path('logout/', Logout, name='Logout')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
