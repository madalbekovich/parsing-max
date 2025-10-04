from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static('static/', document_root=settings.STATIC_ROOT)
    urlpatterns += static('media/', document_root=settings.MEDIA_ROOT)
