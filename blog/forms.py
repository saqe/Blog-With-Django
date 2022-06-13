from django import forms
from .models import Post


class FeaturedPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('featured',)


class PublishedPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('published',)
