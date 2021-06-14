from django.shortcuts import render

from django.contrib.admin.views.decorators import staff_member_required

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

# # JUST Alternative way
# def home_view(request):
#     posts = Post\
#         .objects\
#         .filter(published=True)\
#         .order_by('posted_datetime')[:5]

#     return render(
#         request, 
#         'html/home.html',
#         context={
#             'posts':posts,
#             'title':'HomePage'
#         })

class PostListView(ListView):
    model = Post
    template_name='html/home.html'
    paginate_by = 10
    context_object_name = 'posts'
    queryset = Post.objects.filter(published=True,featured=True)

    def post(self,request):
        Post.object.create()

# View post in detail
class PostDetailView(DetailView):
    model = Post
    template_name='html/post.html'
    context_object_name = 'blogpost'
    

# Create a new post
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name='html/form/create_post.html'
    
    fields = ['title','content','tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name='html/form/update_post.html'
    fields = ['title','content','tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # Verify if the user trying to do that is owner of that post
    def test_func(self):
        return self.request.user == self.get_object().author

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post

    # Verify if the user trying to do that is owner of that post
    def test_func(self):
        return 
        (self.request.user == self.get_object().author)\
        or\
        self.request.user.is_superuser


@staff_member_required
def set_post_published(request):
    pass