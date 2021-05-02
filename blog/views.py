from django.shortcuts import render
from django.http import HttpResponse

posts=[{
        'author'    : 'Saqib',
        'title'     : 'First DemoPost',
        'content'   : 'That my first dummy post written in django.',
        'date_posted': '20-08-2021',
    },{
        'author'    : 'Saqib',
        'title'     : 'First DemoPost (Duplicated)',
        'content'   : 'That my duplicated dummy post written in django.',
        'date_posted': '15-05-2021',
    },
]
# Create your views here.
def home(request):
    context={
        'posts':posts,
        'title':'HomePage'
    }
    return render(request, 'blog/home.html',context=context)

def about(request):
    return render(request, 'blog/about.html',)