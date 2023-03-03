from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def startpage(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>You see the startpage.</h1>')
