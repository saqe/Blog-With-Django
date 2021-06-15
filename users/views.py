from django.shortcuts import render, redirect
from django.contrib import messages

from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm

from .models import User
from blog.models import Post

def register(request):
    form = UserRegisterForm(request.POST or None)

    # There will be two types of HTTP requets at register route. 
    # GET & POST requests. 
    # We need to verify and manage both events differently.
    if request.method == 'POST':
        if form.is_valid():
            # get the username from form.
            username = form.cleaned_data.get('username')

            # Finally register the user after processing.
            form.save()

            # Send a flash message to user on front page
            messages.success( request, f'Account register with username {username}! Login now' )

            # Redirected to login page.
            return redirect('login')

    return render(
        request,
        'users/register.html',
        {'form':form}
    )

@login_required
def my_profile(request):
    blog_posts = Post.objects.filter(author=request.user.id)
    return render(
        request,
        'user/my_profile.html',
        {
            'user':request.user,
            'blog_posts':blog_posts,
            'logged_in':True
        }
    )

class PublicProfileDetailView(DetailView):
    model = User
    template_name = 'users/view_public_profile.html'

    def dispatch(self, request, *args, **kwargs):
        print(request.user.id , self.request.user.id)
        if request.user.id == self.request.user.id:
            return redirect('my-profile')            
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blog_posts"] = Post.objects.filter(author=self.request.user.id)
        return context