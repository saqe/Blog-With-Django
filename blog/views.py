from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post

# Create your views here.
def home(request):
    posts = Post\
        .objects\
        .filter(published=True)\
        .order_by('posted_datetime')[:5]

    return render(
        request, 
        'html/home.html',
        context={
            'posts':posts,
            'title':'HomePage'
        })