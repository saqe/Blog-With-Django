from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_profile, name='my-profile'),
    path('<slug:username>', views.PublicProfileDetailView.as_view(),
         name='view-profile'),
]
