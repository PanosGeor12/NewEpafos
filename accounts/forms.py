from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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