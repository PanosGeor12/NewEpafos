from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.Home, name='Home'),
    path('news/post/<int:year>/<int:month>/<int:day>/<slug:post>', views.PostDetails, name='Post_Details'),
    path('news/', views.AllPosts, name='All_Posts')
]
