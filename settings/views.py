from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ProfileNameForm,ProfileBasicInformationForm

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
        }
    )