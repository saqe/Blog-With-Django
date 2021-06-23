from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic import ListView

class DashboardView(PermissionRequiredMixin,TemplateView):
    permission_required = 'is_staff'
    template_name = 'manager_dashboard/dashboard.html'

class UsersList(PermissionRequiredMixin,ListView):
    model = User
    permission_required = 'is_staff'
    template_name = 'manager_dashboard/users.html'