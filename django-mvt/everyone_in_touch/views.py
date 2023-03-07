from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from .models import Teacher


def homepage(request):
    return render(request, 'everyone_in_touch/homepage.html')


class TeacherListView(ListView):
    template_name = 'everyone_in_touch/teachers.html'
    model = Teacher
    paginate_by = 100
    context_object_name = 'teachers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'everyone_in_touch/teachers_detailed.html'
    context_object_name = 'teacher'
    slug_field = 'url'
    slug_url_kwarg = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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


def about_us(request):
    return render(request, 'everyone_in_touch/about_us.html', context={})