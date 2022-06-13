from django.urls import path
from . import views

urlpatterns = [
    # path('',        views.my_profile, name='my-profile'),
    path('', views.update_profile, name='update-profile'),
    path('update_image/', views.ProfileImageUpdateView.as_view(),
         name='update-profile-image'),
    path('change_password/', views.update_profile_password,
         name='update-profile-password'),
    path('change_email/', views.update_user_email, name='update-email'),
]
