from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.models import Profile
from .forms import (
    ProfileNameForm,
    ProfileBasicInformationForm,
    ProfileImageForm)

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
        }
    )

def update_profile_image(request):
    if request.method == 'POST':
        image_form    = ProfileImageForm(
                request.POST,instance=request.user)

        # If the data we are getting, both forms are valid, only then save the data of the form
        if image_form.is_valid():
            image_form.save()
            messages.success(request,f"Dear {request.user.first_name}, your profile image have been successfully updated!")
            return redirect('my-profile')
    else:
        image_form    = ProfileImageForm(instance=request.user)

    return render( 
        request, 
        'settings/update_picture.html',
        {'object' : image_form,}
    )

class UpdateProfileImageView(LoginRequiredMixin,UpdateView):
    model = Profile
    template_name='settings/update_picture.html'

    fields = ('profile_image')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_staff