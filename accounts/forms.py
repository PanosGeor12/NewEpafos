from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import EnrolledStudent, Major, Teacher
from .models import SchoolUser
import datetime

class SchoolUserCreationForm(UserCreationForm):
  password1 = forms.CharField(min_length=8,
                              widget=forms.PasswordInput(attrs={'class':'form_field form-control',
                                                                'id':'pass1_field',
                                                                'placeholder':'enter users password'}))
  password2 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class':'form_field form-control',
                                                                              'id':'pass2_field',
                                                                              'placeholder':'enter users password again'}))
  class Meta(UserCreationForm):
    model = SchoolUser
    fields = (
      'role',
      'username',
      'password1',
      'password2',
      'email',
      'first_name',
      'last_name',
      'phone_number',
      'birthdate',
      'address'
    )  
    yearCalc = (int(datetime.datetime.now().strftime("%Y"))-17)
    widgets = {
      'username' : forms.TextInput(attrs={'class':'form_field form-control',
                                        'id':'user_field',
                                        'placeholder':'enter username'}),
      'email' : forms.EmailInput(attrs={'class':'form_field form-control',
                                        'id':'email_field',
                                        'placeholder':'enter users email address'}),
      'first_name' : forms.TextInput(attrs={'class':'form_field form-control',
                                            'id':'first_name',
                                            'placeholder':'enter users firstname'}),
      'last_name' : forms.TextInput(attrs={'class':'form_field form-control',
                                           'id':'last_name',
                                           'placeholder':'enter users lastname'}),
      'phone_number' : forms.TextInput(attrs={'class':'form_field form-control ',
                                              'id':'phone_field',
                                              'placeholder':'enter users phone number'}),
      'birthdate' : forms.SelectDateWidget(years=range(1940,yearCalc),
                                           attrs={'class':'date_widget form-select w-25', 
                                                  'id':'birthdate_field'}),
      'address' : forms.TextInput(attrs={'class':'form-field form-control',
                                         'id':'address_field',
                                         'placeholder':'enter users address'})
    } 

class SchoolUserChangeForm(UserChangeForm):
  class Meta:
    model = SchoolUser
    fields = UserChangeForm.Meta.fields
  
class LoginForm(forms.Form):
  username = forms.CharField(max_length=100,
                            required=True, 
                            widget=forms.TextInput(attrs={'class':'form_field form-control',
                                                          'id':'user_field',
                                                          'placeholder':'enter username'}))
  password = forms.CharField(min_length=8,
                            widget=forms.PasswordInput(attrs={'class':'form_field form-control',
                                                              'id':'pass1_field',
                                                              'placeholder':'enter users password'}))
  class Meta:
    model = SchoolUser
    fields = ('username', 'password')

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
    }
  