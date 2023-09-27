from .models import *
from django.views import generic
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(generic.ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'blog_detail.html'
       
class AddBlog(LoginRequiredMixin, generic.CreateView):
    model = Post
    form_class = BlogForm
    template_name = 'add_blog.html'
class UpdateBlog(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_blog.html'

class DeleteBlog(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'blog_detail.html'
    success_url = reverse_lazy('blog-home')



