from django.shortcuts import render
from .models import *
from django.views import generic

# Create your views here.

class Home(generic.ListView):
    model = Post
    template_name = 'blogs/home.html'

class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'blogs/blog_detail.html'

class AddBlog(generic.CreateView):
    model = Post
    template_name = 'blogs/add_blog.html'
    fields = ('title', 'author', 'content')

def login(request):
    return render(request, 'blogs/login.html')
