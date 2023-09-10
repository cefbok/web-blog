from django.shortcuts import render
from .models import *
from django.views import generic

# Create your views here.

class Home(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogs/home.html'

class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'blogs/blog_detail.html'

def login(request):
    return render(request, 'blogs/login.html')
