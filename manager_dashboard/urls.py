from django.urls import path
from django.views.generic import TemplateView

from users.views import (
    UserDeleteView,
    UserAccessStatus,
    UserStaffStatus,)

from blog.views import (
    PostFeaturedAdminUpdate,
    PostPublishedAdminUpdate,
)
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
    path('members/<int:pk>/delete', UserDeleteView.as_view(),  name='delete-member'),
    path('members/<int:pk>/staff-status',  UserStaffStatus.as_view(), name='staff-update'),
    path('members/<int:pk>/access',  UserAccessStatus.as_view(), name='member-access'),

    path('posts/',           PostListView.as_view(), name='articles'),
    path('posts/published/', PublishedPostListView.as_view(), name='published-articles'),
    path('posts/draft/',     DraftPostListView.as_view(),     name='drafted-articles'),
    path('posts/featured/',  FeaturedPostListView.as_view(),  name='featured-articles'),
    path('posts/<slug:slug>/feature-post',  PostFeaturedAdminUpdate.as_view(), name='feature-a-post'),
    path('posts/<slug:slug>/publish-post',  PostPublishedAdminUpdate.as_view(), name='publish-a-post'),
]