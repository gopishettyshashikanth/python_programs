from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^input$', views.input, name="input"),
    url(r'^add$', views.add, name="add"),
    
]