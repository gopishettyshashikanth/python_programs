from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^home/$', views.index, name='index'),
    url(r'^upload/csv/$',views.upload_csv, name='upload_csv'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)