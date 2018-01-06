from django.conf.urls import include, url
from django.contrib import admin
from views import getinput,add,postinput


urlpatterns = [
    url(r'^getinput$', getinput.as_view()),
    url(r'^postinput$', postinput.as_view()),
    url(r'^add$',add.as_view()),
    
]