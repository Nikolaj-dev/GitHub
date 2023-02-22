from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views import View
from django.contrib.auth.models import User
from django.core.cache.backends.locmem import LocMemCache


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Django app running...")


def json_index(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"data": "anydata"}, safe=False, status=201)


def homepage(request: HttpRequest) -> HttpResponse:

    return render(request, 'index.html')


class GetUsers(View, LocMemCache):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        print(User.objects.filter(is_active=True))
        return HttpResponse("Hello World!")
