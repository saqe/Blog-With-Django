from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField()
    last_name = forms.CharField()

    # Nested namespaces for configuration
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name' ,'email', 'password1', 'password2']