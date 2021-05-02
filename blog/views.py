from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'author'    : 'Saqib',
        'title'     : 'First DemoPost',
        'content'   : 'Curabitur placerat augue faucibus viverra fringilla. Vivamus tortor libero, tincidunt vel fermentum et, ultrices at tellus. Vestibulum dictum enim faucibus justo elementum rhoncus. Sed dictum dapibus iaculis. Aliquam eget orci sit amet tortor sodales bibendum in eget nibh. Proin mi lacus, porta ac odio vel, semper accumsan lectus. Morbi ex eros, tincidunt id laoreet vel, viverra in purus. Vestibulum vitae elit et magna pretium pellentesque.',
        'date_posted': 'January 1, 2021',
        'tags'      : ['Tag1','Tag1','Tag1','Tag1','Tag1','Tag1','Tag1',]
    },{
        'author'    : 'Saqib',
        'title'     : 'Second DemoPost title for post',
        'content'   : 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. ',
        'date_posted': 'May 5, 2021',
        'tags'      : ['Tag1','Tag1','Tag1','Tag1','Tag1','Tag1','Tag1',]
    },
]

# Create your views here.
def home(request):
    context={
        'posts':posts,
        'title':'HomePage'
    }
    return render(request, 'html/home.html',context=context)

# def about(request):
#     return render(request, 'blog/about.html',)