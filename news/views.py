from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import NewPost, EditSchoolPost
from .models import Post
from accounts.views import manager_required

@manager_required
def CreatePost(request):
  if request.method == 'POST':
    post_form = NewPost(request.POST)
    if post_form.is_valid():
      post = post_form.save(commit=False)
      post.author = request.user
      post.published = timezone.now()
      post.save()
      return redirect('core:Home')
  else:
    post_form = NewPost()
  return render(request, 'manager/addpost.html', {'post_form':post_form})

@manager_required
def EditPost(request, id):
  post = get_object_or_404(Post, id=id)
  if request.method == 'POST':
    post_form = EditSchoolPost(request.POST, instance=post)
    if post_form.is_valid():
      post_form.save()
      return redirect('news:Manager_Post_Details', post.published.year, post.published.month, post.published.day, post.slug)
  else:
    post_form = EditSchoolPost(instance=post)
  return render(request, 'manager/editpost.html',{'post':post, 
                                                       'post_form':post_form})  

@manager_required
def ManagerPostDetails(request, year, month, day, post):
  post = get_object_or_404(Post, 
                          slug = post,
                          published__year = year,
                          published__month = month, 
                          published__day = day)

  return render(request, 'manager/details.html', {'post':post})

@login_required
def PostDetails(request, year, month, day, post):
  post = get_object_or_404(Post, 
                          status=Post.Status.PUBLISHED,
                          slug = post,
                          published__year = year,
                          published__month = month, 
                          published__day = day)

  return render(request, 'news/details.html', {'post':post})

@manager_required
def ManagePosts(request):
  all_posts = Post.objects.all()
  categories = Post.Categories.choices
  selected_category = request.GET.get('category', 'all')
  
  if selected_category != 'all':
    posts = Post.objects.filter(category=selected_category)
  
  else:
    posts = all_posts
  return render(request, 'manager/manageposts.html', {'posts':posts, 
                                                           'categories':categories})

@login_required
def SchoolPosts(request):
  posts = Post.objects.filter(status=Post.Status.PUBLISHED)
  if request.user.role == 'Teacher':
    return render(request, 'teacher/teachernews.html',{'posts':posts})
  elif request.user.role == 'Student':
    return render(request, 'student/studentnews.html',{'posts':posts})