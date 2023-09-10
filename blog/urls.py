from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='blog-login'),
    path('', views.Home.as_view(), name='blog-home'),
    path('details/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
]