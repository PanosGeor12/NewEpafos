from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import SchoolUser
from .forms import SchoolUserChangeForm, SchoolUserCreationForm
from django import forms
from .models import EnrolledStudent, Major, Teacher
import datetime

class SchoolUserAdmin(UserAdmin):
  add_form = SchoolUserCreationForm
  form = SchoolUserChangeForm
  model = SchoolUser
  list_display = [
    'username',
    'role',
    'first_name',
    'last_name',
    'email',
    'is_staff'
  ]
  readonly_fields=('role',)
  fieldsets = (('User Info', {'fields':('username','password',)}),
              ('Personal Info',{'fields':('role','first_name', 'last_name', 'birthdate')}),
              ('Contact Info', {'fields':('phone_number','email')}))
  add_fieldsets = (('User Info', {'fields':('username', 'password1', 'password2')}),
                   ('Personal Info', {'fields':('role', 'first_name', 'last_name','birthdate')}),
                   ('Contact Info', {'fields':('email', 'phone_number')}))

admin.site.register(SchoolUser, SchoolUserAdmin)
admin.site.register(EnrolledStudent)
admin.site.register(Teacher)