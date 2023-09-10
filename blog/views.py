from django.shortcuts import render
from .models import *
from django.views import generic
from .forms import *

# Create your views here.

class Home(generic.ListView):
    model = Post
    template_name = 'blogs/home.html'

class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'blogs/blog_detail.html'

class AddBlog(generic.CreateView):
    model = Post
    form_class = BlogForm
    template_name = 'blogs/add_blog.html'

class UpdateBlog(generic.UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blogs/update_blog.html'

def login(request):
    return render(request, 'blogs/login.html')
