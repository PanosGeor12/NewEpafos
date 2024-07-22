from django.shortcuts import render, get_object_or_404
from news.models import Post

def Home(request):
  latest_posts = Post.objects.filter(status=Post.Status.PUBLISHED)[:3]

  return render(request, 'index.html', {'latest_posts': latest_posts})

def PostDetails(request, year, month, day, post):
  post = get_object_or_404(Post, 
                          status=Post.Status.PUBLISHED,
                          slug = post,
                          published__year = year,
                          published__month = month, 
                          published__day = day)
  recent_posts = Post.objects.filter(status= Post.Status.PUBLISHED, category = post.category).exclude(id=post.id)[:3]

  return render(request, 'core/news/details.html', {'post':post, 
                                                    'recent_posts':recent_posts})

def AllPosts(request):
  posts = Post.objects.filter(status=Post.Status.PUBLISHED)

  return render(request, 'core/news/news.html', {'posts':posts})

