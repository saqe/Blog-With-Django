"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
# For Adding static files for media route for development stage
from django.conf import settings
from django.conf.urls.static import static
# Using pre-build Auth Route
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import TemplateView
from users.views import register as RegisterationView
# Custom Views
from blog import views as blogViews

urlpatterns = [
    path('admin/' , admin.site.urls),
    path(''  , include('blog.urls'),name='blog'),

    path('about/'    , TemplateView.as_view(template_name="html/about.html"), name='blog-about'),

    path('register/' , RegisterationView , name='user-register'),
    path('login/'    , LoginView.as_view(template_name  = 'html/login.html',redirect_authenticated_user=True), name='login'),
    path('logout/'   , LogoutView.as_view()   , name='logout'),

    path('profile/'  , include('users.urls'), name='profile'),
] 

# Only run this for development server
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)