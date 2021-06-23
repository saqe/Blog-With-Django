from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import (
    DashboardView,
    UsersList,
)

urlpatterns=[
    # path('',        views.my_profile, name='my-profile'),
    path('', DashboardView.as_view(), name='manager-dashboard'),
    path('users/', UsersList.as_view(), name='users-list'),
    # path('users/update_status/', views., name=''),
    # path('users/update_role/', views., name=''),
    # path('posts/', views., name=''),
    # path('posts/update_status', views., name=''),
]