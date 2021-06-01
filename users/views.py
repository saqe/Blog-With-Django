from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logoutSession
from django.contrib.auth.forms import UserChangeForm
from users.forms import UserRegisterForm

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
            messages.success(
                request,
                f'Account register with username {username}! Login now'
            )

            # Redirected to login page.
            return redirect('login')

    return render(
        request,
        'html/register.html',
        {'form':form}
    )

def logout(request):
    messages.info(request,'You have been logged out.')
    logoutSession(request)
    return redirect('login')

@login_required
def profile(request):
    form = UserChangeForm()
    return render(
        request,
        'html/profile.html',
        {'form':form}
    )