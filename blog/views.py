from django.shortcuts import render

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

def home(request):
    posts = Post\
        .objects\
        .filter(published=True)\
        .order_by('posted_datetime')[:5]

    return render(
        request, 
        'html/home.html',
        context={
            'posts':posts,
            'title':'HomePage'
        })
class PostListView(ListView):
    model = Post
    template_name='html/home.html'
    paginate_by = 10
    context_object_name = 'posts'
    queryset = Post.objects.filter(published=True)

class PostDetailView(DetailView):
    model = Post
    template_name='html/post.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name='html/post_form.html'
    fields = ['title','content','tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name='html/post_form.html'
    fields = ['title','content','tags']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().author

class PostDeleteView(DeleteView):
    model = Post