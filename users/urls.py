from django.urls import path
from . import views

urlpatterns=[
    path('',views.my_profile, name='my-profile'),
    path('<int:pk>', views.PublicProfileDetailView.as_view(), name='view-profile'),
]