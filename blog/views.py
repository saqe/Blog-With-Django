from django.shortcuts import render

from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin)

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,)

from .models import Post

class PostListView(ListView):
    model = Post
    template_name='blog/home.html'
    paginate_by = 10
    context_object_name = 'blog_posts'
    queryset = Post.objects.filter(published=True,featured=True)

# View post in detail
class PostDetailView(DetailView):
    model = Post
    template_name='blog/post.html'
    context_object_name = 'blogpost'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_in_user"] = self.request.user
        return context
    

# Create a new post
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name='blog/form/create_post.html'
    
    fields = ['title','content','tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name='blog/form/update_post.html'
    fields = ['title','content','tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # Verify if the user trying to do that is owner of that post
    def test_func(self):
        return (self.request.user == self.get_object().author) or self.request.user.is_staff

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name='blog/form/delete_post.html'
    success_url = reverse_lazy('my-profile')
    # Verify if the user trying to do that is owner of that post
    def test_func(self):
        return (self.request.user == self.get_object().author) or self.request.user.is_staff