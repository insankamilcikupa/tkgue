from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'judul' : 'belajar asik',
        'kontributor' : 'asri',
        'banner':'img/banner_home.png',
        'nav' : [
            ['/' , 'Home'],
            ['/blog' , 'Blog'],
            ['/about' , 'About'],
            ['/contact', 'Contact']
        ]
    }
    return render(request,'index.html', context)
