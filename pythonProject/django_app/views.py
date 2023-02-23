import time
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views import View
from django.contrib.auth.models import User
from django.core.cache import caches


LocMemCache = caches["default"]


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Django app running...")


def json_index(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"data": "anydata"}, safe=False, status=201)


def homepage(request: HttpRequest) -> HttpResponse:

    return render(request, 'index.html')


class GetUsers(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        time_start = time.perf_counter()
        users = LocMemCache.get("users")
        cache_res = "Has cache"
        if not users:
            cache_res = "No cache"
            users = User.objects.all()
            LocMemCache.set("users", users, timeout=5)
        time_end = time.perf_counter()
        return HttpResponse(f"{time_end-time_start}, {cache_res}")
