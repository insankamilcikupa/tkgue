from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul' : 'belajar asik di blog',
        'kontributor' : 'mala',
        'banner':'blog/img/banner_blog.png',
        'app_css': 'blog/css/styles.css',
        'nav' : [
            ['/' , 'Home'],
            ['/blog' , 'Blog'],
            ['/about' , 'About'],
            ['/contact', 'Contact']
        ]
    }
    return render(request,'blog/index.html', context)

def recent(request):
    context = {
        'judul' : 'recent post',
        'kontributor' : 'male',
    }
    return render(request,'blog/index.html', context)

def news(request):
    context = {
        'judul' : 'ini halaman news',
        'kontributor' : 'malo',
    }
    return render(request,'blog/index.html', context)

