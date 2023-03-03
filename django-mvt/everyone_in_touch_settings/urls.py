from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('grapelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('everyone_in_touch.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT,
    )

