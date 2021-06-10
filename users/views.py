from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib import messages

from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logoutSession
from django.contrib.auth.forms import UserChangeForm
from users.forms import (
    UserRegisterForm,
    UpdateNameForm,
    ProfileUpdateForm)

from .models import User

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
        'html/register.html',
        {'form':form}
    )

# def logout(request):
#     messages.info(request,'You have been logged out.')
#     logoutSession(request)
#     return redirect('login')

@login_required
def my_profile(request):
    return render(request, 'html/my_profile.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form    = UpdateNameForm(
                request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(
                request.POST, request.FILES, instance=request.user.profile)

        # If the data we are getting, both forms are valid, only then save the data of the form
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,f"Dear {request.user.first_name}, your profile have been successfully updated!")
            return redirect('my-profile')
    else:
        user_form    = UpdateNameForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render( 
        request, 
        'html/update_profile.html',
        {
            'user_form' : user_form,
            'profile_form' : profile_form,
        }
    )

class ProfileDetailView(DetailView):
    model = User
    template_name = 'html/view_profile.html'

def view_profile(request,userid):
    user = User.objects.get(id=userid)
    return render( 
        request, 
        'html/my_profile.html',
    )