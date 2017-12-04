from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    url(r'^postform/', include('postform.urls')),
    url(r'^services/', include('services.urls')),
    url(r'^admin/', admin.site.urls),
]


urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))