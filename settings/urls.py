from django.urls import path
from . import views
from .views import UpdateProfileImageView

urlpatterns=[
    # path('',        views.my_profile, name='my-profile'),
    path('general/', views.update_profile, name='update-profile'),
    # path('profile_image/', UpdateProfileImageView.as_view(), name='update-profile-image'),
    path('profile_image/', views.update_profile_image, name='update-profile-image'),
    
    # path('password/', views.PublicProfileDetailView.as_view(), name='view-profile'),
]