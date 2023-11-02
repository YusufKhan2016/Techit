from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('orbitor.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)