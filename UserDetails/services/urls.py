from django.conf.urls import include, url
from services import views

urlpatterns = [
   url(r'^userlist/$', views.userlist, name='userlist'),
]