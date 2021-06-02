from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post

# Create your views here.
def home(request):
    context={
        'posts':Post.objects.all(),
        'title':'HomePage'
    }
    # print()
    return render(request, 'html/home.html',context=context)

# def about(request):
#     return render(request, 'blog/about.html',)