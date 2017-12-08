from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [	

	# url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
	url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'forms/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'forms/logged_out.html'}, name='logout'),

    url(r'^signup/$', views.signup, name='signup'),
	
	url(r'^home/$', views.index, name='index'),
	url(r'^login/userlist$', views.user_list, name='user_list'),
	url(r'^login/add$', views.user_add, name='user_add'),
	url(r'^login/(?P<pk>\d+)/$', views.user_view_detail, name='user_view_detail'),
	url(r'^login/(?P<pk>\d+)/edit/$', views.user_edit, name='user_edit'),
	url(r'^login/(?P<id>\d+)/delete$', views.user_delete, name='user_delete'),

	url(r'^login/search$', views.user_search, name='user_search'),
]
