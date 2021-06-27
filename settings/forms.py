from django.db import models
from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import ugettext as _

# Django Model Custom Fields
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

# Custom import
from users.models import Profile

class ProfileBasicInformationForm(forms.ModelForm):
    # Profile Image
    # profile_image = forms.ImageField(
    #     label=_('Profile Image'),
    #     required=False,
    #     error_messages = {'invalid':_("Image files only")}, 
    #     widget=forms.FileInput)

    country = CountryField()
    class Meta:
        model = Profile
        fields = ('gender','job_role','phone_number','country','address','state','city','zip_code')


class ProfileImageForm(forms.ModelForm):
    profile_image = forms.ImageField()

    profile_image = forms.ImageField(
        label=_('Profile Image'),
        required=False,
        error_messages = {'invalid':_("Image files only")}, 
        widget=forms.FileInput)
        
    class Meta:
        model = Profile
        fields = ("profile_image",)

class ProfileNameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class UserEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']