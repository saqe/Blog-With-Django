from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,)

urlpatterns=[
    path('',PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/'       ,PostDetailView.as_view(), name='view-blog-post'),
    path('post/create/'            ,PostCreateView.as_view(), name='create-blog-post'),
    path('post/update/<int:pk>' ,PostUpdateView.as_view(), name='update-blog-post'),
    path('post/delete/<int:pk>' ,PostDeleteView.as_view(), name='delete-blog-post'),
]