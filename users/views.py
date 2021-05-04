from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def register(request):
    # There will be two types of HTTP requets at register route. 
    # GET & POST requests. 
    # We need to verify and manage both events differently.
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f'Account created with username {username}!'
            )
            return redirect('blog-home')
    else:
        form = UserCreationForm()

    return render(
        request,
        'html/register.html',
        {'form':form}
    )

def login(request):
    return HttpResponse('login page')

def logout(request):
    return HttpResponse('logout page')

@login_required
def profile(request):
    return HttpResponse('profile page')