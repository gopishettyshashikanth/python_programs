from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^home/$', views.index, name='index'),
	url(r'^login$', views.user_list, name='user_list'),
	url(r'^login/add$', views.user_add, name='user_add'),
	url(r'^login/(?P<pk>\d+)/$', views.user_view_detail, name='user_view_detail'),
	url(r'^login/(?P<pk>\d+)/edit/$', views.user_edit, name='user_edit'),
	url(r'^login/(?P<id>\d+)/delete$', views.user_delete, name='user_delete'),

	url(r'^login/search$', views.user_search, name='user_search'),
]
