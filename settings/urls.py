from django.urls import path
from . import views

urlpatterns=[
    # path('',        views.my_profile, name='my-profile'),
    path('general/', views.update_profile, name='update-profile'),
    # path('profile_image/', views.PublicProfileDetailView.as_view(), name='view-profile'),
    # path('password/', views.PublicProfileDetailView.as_view(), name='view-profile'),
]