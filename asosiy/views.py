from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout


def register(sorov):
    if sorov.method == 'POST' and sorov.POST.get('p') == sorov.POST.get('p2'):
        User.objects.create_user(
            username = sorov.POST.get('l'),
            password = sorov.POST.get('p')
        )
        return redirect('login')
    return render(sorov,'register.html')


def login_view(sorov):
    if sorov.method == 'POST':
        user = authenticate(
            username = sorov.POST.get('l'),
            password = sorov.POST.get('p')
        )
        if user is None:
            return redirect('login')
        login(sorov,user)
        return redirect('/maqolalar/')
    return render(sorov,'login.html')


def logout_view(sorov):
    logout(sorov)
    return redirect("/")


def blog_view(sorov):
    if sorov.method == 'POST':
        Maqola.objects.create(
            sarlavha=sorov.POST.get('sarlavha'),
            mavzu=sorov.POST.get('mavzu'),
            matn=sorov.POST.get('matn'),
            muallif=Muallif.objects.get(user=sorov.user)
        )
        return redirect("/maqolalar/")
    if sorov.user.is_authenticated:
        content = {
            "maqolalar":Maqola.objects.filter(muallif__user = sorov.user)
        }
        return render(sorov,'maqola.html', content)
    return redirect('/')


def bitta_maqola(sorov,son):
    content = {
        "maqola":Maqola.objects.get(id = son, muallif__user = sorov.user)
    }
    return render(sorov,'maqola.html',content)