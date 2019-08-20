from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from.models import Orang, Nilai, SPP
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul':'ABOUT',
        'subjudul':'Tentang website belajar asik',
        'banner':'img/banner_about.png',
        'app_css': 'about/css/styles.css',
        'nav' : [
            ['/' , 'Home'],
            ['/blog' , 'Blog'],
            ['/about' , 'About'],
            ['/contact', 'Contact']
        ]
    }

    template_name = None
    if request.user.is_authenticated():
        template_name = 'about/semua.html'
    else:
        template_name = 'about/index.html'

    return render(request, 'about/index.html', context)

def loginView(request):
    context = {
        'judul':'Login',
        'app_css': 'about/css/styles.css',
        'nav' : [
            ['/' , 'Home'],
            ['/blog' , 'Blog'],
            ['/about' , 'About'],
            ['/contact', 'Contact']
        ]
    }

    user = None

    if request.method == "GET":
        if request.user.is_authenticated():
            return redirect('semua')
        else:
            return render(request, 'about/login.html', context)

    if request.method == "POST":
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(request, username=username_login, password=password_login)

        if user is not None:
            login(request, user)
            return redirect('semua')
        else:
            return redirect('login')

    return render(request, 'about/login.html', context)

@login_required
def logoutView(request):
    context = {
        'judul' : 'Logout',
    }

    if request.method == "POST":
        if request.POST["logout"] == "Submit Query":
            logout(request)

        return redirect('index')
    
    return render(request, 'about/logout.html', context)


def semua(request):
    context = {
        'judul': 'HALAMAN KHUSUS',
        'app_css': 'about/css/styles.css',
        'nav' : [
            ['/' , 'Home'],
            ['/blog' , 'Blog'],
            ['/about' , 'About'],
            ['/contact', 'Contact']
        ]
    }

    return render(request, 'about/semua.html', context)


def data(request):
    data = Orang.objects.filter(nama = request.user)
    context = {
        'tampil_data':data,
        'app_css': 'about/css/styles.css',
        'nav' : [
            ['/' , 'Home'],
            ['/blog' , 'Blog'],
            ['/about' , 'About'],
            ['/contact', 'Contact']
        ]
    }
    return render(request, 'about/data.html', context)

def nilai(request):
    nilai = Nilai.objects.filter(user = request.user)
    context = {
        'tampil_nilai':nilai,
        'app_css': 'about/css/styles.css',
        'nav' : [
            ['/' , 'Home'],
            ['/blog' , 'Blog'],
            ['/about' , 'About'],
            ['/contact', 'Contact']
        ]
    }
    return render(request, 'about/nilai.html', context)

def spp(request):
    spp = SPP.objects.filter(user = request.user)
    context = {
        'tampil_spp': spp,
        'app_css': 'about/css/styles.css',
        'nav' : [
            ['/' , 'Home'],
            ['/blog' , 'Blog'],
            ['/about' , 'About'],
            ['/contact', 'Contact']
        ]
    }
    return render(request, 'about/spp.html', context)
