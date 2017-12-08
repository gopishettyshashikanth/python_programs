from django.conf.urls import include, url
from services import views

urlpatterns = [
   url(r'^userlists/$', views.userlist, name='userlists'),
   url(r'^deptlist/$', views.deptlist, name='deptlist'),   
   url(r'^checkMobilenumber/$', views.checkMobilenumber, name='checkMobilenumber'),
]