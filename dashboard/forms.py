from django import forms
from django.shortcuts import get_object_or_404
from .models import EnrolledStudent, Major, Teacher
from accounts.models import SchoolUser
from django.contrib.auth.forms import UserChangeForm

class StudentDataForm(forms.ModelForm):
  major = forms.ModelChoiceField(queryset=Major.objects.all(), widget=forms.Select(attrs={'class':'select-form'}))
  class Meta:
    model = EnrolledStudent
    fields = ('student_id', 'major') 
    widgets = {
      'student_id' : forms.TextInput(attrs={'placeholder':'enter students id',
                                                                          'class':'form-control student_id_field', 
                                                                          'id':'studentID',
                                                                     'max_length':'4'})
    }

class TeacherDataForm(forms.ModelForm):
  class Meta:
    model = Teacher
    fields = ('teacher_id', 'occupation')
    widgets = {
      'teacher_id' : forms.TextInput(attrs={'placeholder':'enter teachers id',
                                                          'class':'form-control teacher_id_field',
                                                          'id':'teacherID',
                                                          'maxlength':'10'}),
      'occupation' : forms.TextInput(attrs={'placeholder':'enter users occupation',
                                                                'class':'form-control occupation_field',
                                                                'id':'occupation'})                                 
    }

class EditSchoolUser(UserChangeForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class':'form_field form-control w-50', 'id':'username_field', 'placeholder':'enter users username'}), required=False)
  email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form_field form-control w-50', 'id':'email_field', 'placeholder':'enter users email address'}), required=False)
  first_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form_field form-control w-50', 'id':'first_name', 'placeholder':'enter users firstname'}))
  last_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form_field form-control w-50', 'id':'last_name', 'placeholder':'enter users lastname'}))
  phone_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form_field form-control w-50', 'id':'phone_field', 'placeholder':'enter users phone number'}), required=False)
  address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-field form-control w-50', 'id':'address_field','placeholder':'enter users address'}), required=False)

  class Meta:
    model = SchoolUser
    fields = ('email','username','first_name','last_name','phone_number','address')
  
class EditStudentData(forms.ModelForm):
  major = forms.ModelChoiceField(queryset=Major.objects.all(), required=False)
  class Meta:
    model = EnrolledStudent
    fields = ('major',)

class EditTeacherData(forms.ModelForm):
  class Meta:
    model = Teacher
    fields = ('occupation',)
    widgets = {
      'occupation' : forms.TextInput(attrs = {'placeholder':'enter user occupation',
                                            'class':'form-control occupation_field w-50',
                                            'id':'occupation'}),
      # 'teacher_id' : forms.TextInput(attrs = {'placeholder':'enter teachers id',
      #                                       'class':'form-control teacher_id_field w-50',
      #                                       'id':'teacherID'})
    }
  
