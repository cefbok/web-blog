from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import generic
from .forms import *
from django.urls import reverse_lazy

# Create your views here.

class Home(generic.ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'blog_detail.html'

class AddBlog(generic.CreateView):
    model = Post
    form_class = BlogForm
    template_name = 'add_blog.html'

class UpdateBlog(generic.UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_blog.html'

class DeleteBlog(generic.DeleteView):
    model = Post
    template_name = 'blog_detail.html'
    success_url = reverse_lazy('blog-home')

