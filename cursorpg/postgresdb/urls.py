from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [	

	url(r'^dashboard/$', views.dashboard, name='dashboard'),	
]
