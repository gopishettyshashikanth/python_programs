from django.conf.urls import include, url
from . import views
from views import student_form

urlpatterns = [
    
    url(r'^student_details$', views.StudentDetails.as_view(), name='get_student_details'),
    url(r'^student_details/(?P<std_id>\d+)/update$', views.StudentDetails.as_view(), name='update_student_details'),
    url(r'^student_details/create$', views.StudentDetails.as_view(), name='create_student_details'),
    url(r'^student_details/(?P<std_id>\d+)/delete/$', views.StudentDetails.as_view(), name="delete_student_details"),
   	

   	url(r'^students$', views.student_list, name='student_list'),    
    url(r'^(?P<id>\d+)$', views.student_form, name='student_edit'),
    url(r'^(?P<id>\d+)/view$', views.student_form, name='student_view'),
    url(r'^(?P<id>\d+)/delete$', views.student_delete, name='student_delete'),

    url(r'^student/new$', views.student_form, name='student_add'),

 	
]

