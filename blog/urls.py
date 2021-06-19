from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,)

urlpatterns=[
    path('',PostListView.as_view(), name='blog-home'),
    path('post/create/'           , PostCreateView.as_view(), name='create-blog-post'),
    path('post/update/<slug:slug>', PostUpdateView.as_view(), name='update-blog-post'),
    path('post/delete/<slug:slug>', PostDeleteView.as_view(), name='delete-blog-post'),
    # At last with least priority
    path('post/<slug:slug>/'      , PostDetailView.as_view(), name='view-blog-post'),
]