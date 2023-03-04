from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User


def startpage(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>You see the startpage.</h1>')


def homepage(request):
    return render(request, 'everyone_in_touch/homepage.html')


def login_(request):
    if request.method == 'POST':
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('homepage', args=()))
        else:
            raise Exception("Login or password is incorrect!")
    return render(request, 'everyone_in_touch/login.html', context={})


def sign_up(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect(reverse('homepage', args=()))
    return render(request, 'everyone_in_touch/sign_up.html', context={})


def logout_(request):
    logout(request)
    return redirect(reverse('homepage', args=()))