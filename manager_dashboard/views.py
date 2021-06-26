from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from blog.models import Post

class DashboardView(PermissionRequiredMixin,TemplateView):
    permission_required = 'is_staff'
    template_name = 'manager_dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count_published_posts"] = Post.objects.filter(published=True).count()
        context["count_featured_posts"] = Post.objects.filter(featured=True,published=True).count()
        context["count_pending_posts"] = Post.objects.filter(published=False).count()
        context["count_members"] = User.objects.count()
        return context
    
class MembersList(PermissionRequiredMixin,ListView):
    permission_required = 'is_staff'
    template_name = 'manager_dashboard/members.html'
    model = User


class PostListView(PermissionRequiredMixin,ListView):
    permission_required = 'is_staff'
    template_name = 'manager_dashboard/articles-table.html'
    model = Post

class PublishedPostListView(PermissionRequiredMixin,ListView):
    permission_required = 'is_staff'
    template_name = 'manager_dashboard/articles-table.html'
    model = Post
    queryset = Post.objects.filter(published=True)

class DraftPostListView(PermissionRequiredMixin,ListView):
    permission_required = 'is_staff'
    template_name = 'manager_dashboard/articles-table.html'
    model = Post
    queryset = Post.objects.filter(published=False)

class FeaturedPostListView(PermissionRequiredMixin,ListView):
    permission_required = 'is_staff'
    template_name = 'manager_dashboard/articles-table.html'
    model = Post
    queryset = Post.objects.filter(published=True,featured=True)