from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import (
    DashboardView,
    MembersList,
    PostListView,
    PublishedPostListView,
    DraftPostListView,
    FeaturedPostListView,
)

urlpatterns=[
    # path('',        views.my_profile, name='my-profile'),
    path('', DashboardView.as_view(), name='admin-area'),
    path('members/', MembersList.as_view(), name='members-list'),

    path('posts/',           PostListView.as_view(), name='articles'),
    path('posts/published/', PublishedPostListView.as_view(), name='published-articles'),
    path('posts/draft/',     DraftPostListView.as_view(),     name='drafted-articles'),
    path('posts/featured/',  FeaturedPostListView.as_view(),  name='featured-articles'),

    # path('users/update_role/', views., name=''),
    # path('posts/update_status', views., name=''),
]