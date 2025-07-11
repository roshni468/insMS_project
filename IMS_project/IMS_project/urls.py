# File: IMS_project/urls.py
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from auth_user.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth_user.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
