from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from accounts.models import Major, SchoolUser
from .models import Exercise

class AddNewExercise(forms.ModelForm):
  description = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False )
  class Meta:
    model = Exercise
    fields = '__all__'
    widgets = {
      'name': forms.TextInput(attrs={'class':'form-control w-50'}),
      'slug': forms.TextInput(attrs={'class':'form-control w-50'}),
      'uploaded_files': forms.FileInput(attrs={'class':'form-control w-50', 'type':'file', 'id':'formFile'}),
      'deadline' : forms.DateTimeInput(attrs={'class':'form-control w-25','type':'datetime-local'})
    }