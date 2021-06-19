from django.urls import include,path
from rest_framework import routers

# Custom Views
from .views import BlogViewSet

# DRF Router
router = routers.DefaultRouter()

# Registered a route for posts in API.
router.register('articles', BlogViewSet)

# router.register('profile', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]