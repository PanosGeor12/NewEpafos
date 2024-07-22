from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Post
from accounts.models import SchoolUser

class NewPost(forms.ModelForm):
  category = forms.ChoiceField(choices=Post.Categories.choices, widget=forms.Select(attrs={'class': 'form-select w-25', 'id': 'category_field'}))
  status = forms.ChoiceField(choices=Post.Status.choices, widget=forms.Select(attrs={'class': 'form-select w-25', 'id': 'status_field'}))
  body = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
  class Meta:
    model = Post
    fields = ('title','category', 'slug', 'body', 'status')
    widgets = {
      'title' : forms.TextInput(attrs={'class': 'form-control w-50', 'id': 'post_title'}),
      'slug' : forms.TextInput(attrs={'class': 'form-control', 'id': 'post_slug '}),
    }

class EditSchoolPost(forms.ModelForm):
  category = forms.ChoiceField(choices=Post.Categories.choices, widget=forms.Select(attrs={'class': 'form-select w-25', 'id': 'category_field'}))
  status = forms.ChoiceField(choices=Post.Status.choices, widget=forms.Select(attrs={'class': 'form-select w-25', 'id': 'status_field'}))
  body = forms.CharField(widget=CKEditor5Widget(config_name='extends'), required=False)
  class Meta:
    model = Post
    fields = ('title', 'category', 'slug', 'body','status')
    widgets = {
      'title' : forms.TextInput(attrs={'class': 'form-control w-50', 'id': 'post_title'}),
      'slug' : forms.TextInput(attrs={'class': 'form-control', 'id': 'post_slug '}),
    }