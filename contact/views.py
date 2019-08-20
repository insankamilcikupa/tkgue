from django.shortcuts import render

# Create your views here.

from.models import Kontak

def index(request):
    kontak = Kontak.objects.all()

    context = {
        'datanya' : kontak,
        'judul' : 'belajar asik di blog',
        'kontributor' : 'mala',
        'banner':'contact/img/banner_contact.png',
        'app_css': 'contact/css/styles.css',
        'nav' : [
            ['/' , 'Home'],
            ['/blog' , 'Blog'],
            ['/about' , 'About'],
            ['/contact', 'Contact']
        ]
    }
    return render(request,'contact/index.html', context)

