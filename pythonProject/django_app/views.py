import time
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views import View
from django.contrib.auth.models import User
from django.core.cache import caches
from .models import Todos


LocMemCache = caches["default1"]


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Django app running...")


def json_index(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"data": "anydata"}, safe=False, status=201)


def homepage(request: HttpRequest) -> HttpResponse:
    users = User.objects.all()
    return render(request, 'index.html', context={"users": users})


class GetUsers(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        time_start = time.perf_counter()
        users = LocMemCache.get("users")
        cache_res = "Has cache"
        if not users:
            cache_res = "No cache"
            users = User.objects.all()
            LocMemCache.set("users", users, timeout=60)
        time_end = time.perf_counter()
        return JsonResponse(
            {
                "time": f"{time_end-time_start}",
                "cacheResult": f"{cache_res}",
                "users": [user.username for user in users]}
        )


class GetTodos(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        time_start = time.perf_counter()
        todos = LocMemCache.get("todos")
        cache_res = "Has cache"
        if not todos:
            cache_res = "No cache"
            todos = Todos.objects.all()
            LocMemCache.set("todos", todos, timeout=60)
        time_end = time.perf_counter()
        return JsonResponse(
            {
                "time": f"{time_end - time_start}",
                "cacheResult": f"{cache_res}",
                "todos": [todo.title for todo in todos]}
        )

