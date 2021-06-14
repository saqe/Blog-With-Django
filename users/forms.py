from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext as _

from django_countries.fields import CountryField
from .models import Profile
class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    
    # Nested namespaces for configuration
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name' ,'email', 'password1']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']

class UpdateNameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class ProfileUpdateForm(forms.ModelForm):
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
