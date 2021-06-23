from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


from users.models import Profile
from .forms import (
    ProfileNameForm,
    ProfileBasicInformationForm,
    ProfileImageForm,
    UserEmailForm)

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin)

from django.views.generic import (DetailView,UpdateView,)

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form    = ProfileNameForm(
                request.POST,instance=request.user)
        profile_form = ProfileBasicInformationForm(
                request.POST, request.FILES, instance=request.user.profile)

        # If the data we are getting, both forms are valid, only then save the data of the form
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,f"Dear {request.user.first_name}, your profile have been successfully updated!")
            return redirect('my-profile')
    else:
        user_form    = ProfileNameForm(instance=request.user)
        profile_form = ProfileBasicInformationForm(instance=request.user.profile)

    return render( 
        request, 
        'settings/update_profile.html',
        {
            'user_form' : user_form,
            'profile_form' : profile_form,
            'basic_active':True
        }
    )

@login_required
def update_profile_image(request):
    if request.method == 'POST':
        image_form    = ProfileImageForm(
                request.POST,instance=request.user)

        # If the data we are getting, both forms are valid, only then save the data of the form
        if image_form.is_valid():
            image_form.save()
            
            messages.success(request,
                f"Dear {request.user.first_name}, your profile image have been successfully updated!")
            return redirect('my-profile')
    else:
        image_form    = ProfileImageForm(instance=request.user)

    return render( 
        request, 
        'settings/update_picture.html',
        {
            'profile_image_form' : image_form,
            'picture_active':True,
        }
    )

@login_required
def update_profile_password(request):
    if request.method == 'POST':
        password_form    = PasswordChangeForm(request.user,request.POST)
        # If the data we are getting, both forms are valid, only then save the data of the form
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request,f"Dear {request.user.first_name}, your password have been successfully updated!")
            return redirect('my-profile')
    else:
        password_form    = PasswordChangeForm(request.user)

    return render( 
        request, 
        'settings/update_password.html',
        {
            'password_form' : password_form,
            'password_active' : True
        }
    )


@login_required
def update_user_email(request):
    if request.method == 'POST':
        email_form    = UserEmailForm(
            request.POST, instance=request.user)
        # If the data we are getting, both forms are valid, only then save the data of the form
        if email_form.is_valid():
            user = email_form.save()
            messages.success(request,f"Dear {request.user.first_name}, your email have been successfully updated!")
            return redirect('my-profile')
    else:
        email_form    = UserEmailForm(instance=request.user)

    return render( 
        request, 
        'settings/update_email.html',
        {
            'email_form' : email_form,
            'email_active' : True
        }
    )