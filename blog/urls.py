from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='blog-home'),
    path('details/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),


    # add, update, delete post
    path('add-blog/', views.AddBlog.as_view(), name='blog-add'),
    path('details/edit/<int:pk>/', views.UpdateBlog.as_view(), name='blog-edit'),
    path('details/<int:pk>/delete/', views.DeleteBlog.as_view(), name='blog-delete'),
]