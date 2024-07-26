from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('manager/', views.ManagerHome, name='Manager_Home'),
    path('student/', views.StudentHome, name='Student_Home'),
    path('teacher/', views.TeacherHome, name='Teacher_Home'),
]
