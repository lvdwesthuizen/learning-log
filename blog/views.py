from django.shortcuts import render
from blog.models import Post, Comment

# Create your views here.
def blog_index(request):
   # obtain a queryset containing all posts in the database
   # The minus sign (-) tells Django to start with the largest value rather than the smallest
   posts = Post.objects.all().order_by("-created_on")
   # define a context dictionary
   context = {
      "posts": posts,
   }
   # render a template named index.html
   return render(request, "blog/index.html", context)

def blog_category(request, category):
   posts = Post.objects.filter(
      categories__name__contains=category
   ).order_by("-created_on")
   context = {
      "category": category,
      "posts": posts,
   }
   return render(request, "blog/index.html", context)

def blog_detail(request, pk):
   # retrieves the object with the given primary key - the unique identifier in the db
   post = Post.objects.get(pk=pk)
   comments = Comment.objects.filter(post=post)
   context = {
      "post": post,
      "comments": comments,
   }
   return render(request, "blog/detail.html", context)