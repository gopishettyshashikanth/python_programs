from django.shortcuts import render
from userapp.models import *
from rest_framework.views import APIView 
from rest_framework.response import Response
from userapp.user_serializer import StudentSerializer
from django.views.generic import TemplateView, FormView
from django.shortcuts import render_to_response, render, redirect, HttpResponseRedirect, Http404, HttpResponse
from django.template import Template, Context, RequestContext
from .forms import StudentForm
from django.core.urlresolvers import resolve, reverse
from django.contrib import messages
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
def format_serializer_errors(**kwargs):
    errors_list = []
    for key , val in kwargs.items():
        str1 = " ".join(val)
        str1 = key + " : " + str1
        error_dict = {"field_name" : key, key : str1}
        errors_list.append(error_dict)
    return errors_list

class StudentDetails(APIView):

    def get(self,request,std_id=None):
        try:
            if std_id:
                std_obj = Student.objects.filter(id=std_id)
            else:
                std_obj = Student.objects.all()
            std_list = std_obj.values('id','name','dob','gender')
            context_data = {"success":True,"data":std_list}
        except Exception as e:
            context_data = {"success" : False, "errors" : {"message":str(e)}}
        return Response(context_data)

    def post(self,request,std_id=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(): 
            if std_id:
                try:
                    std_obj = Student.objects.get(id=std_id)
                    std_obj.name = request.data['name']
                    std_obj.gender = request.data['gender']
                    std_obj.dob = request.data['dob']
                    std_obj.save()
                    context_data = {"success":True,"data":"Record Updated Succefully"}
                except Exception as e:
                    pass    
            else:
                kwargs ={
                    "name":request.data['name'],
                    "gender":request.data['gender'],
                    "dob" : request.data['dob']
                }   
                std_obj = Student.objects.create(**kwargs)
                context_data = {"success":True,"data":"Record Created Succefully"}
        else:
            errors_list =  format_serializer_errors(**serializer.errors)
            context_data = {"success" : False, "errors" : {"message": "Validation Error" ,  "errors_list" : errors_list}}
        return Response(context_data)
    def delete(self,request,std_id=None,format=None):
        print "cmng delete"
        try:
            std_obj = Student.objects.get(id=std_id)
            print std_obj,"std_obj"
            std_obj.delete()
            context_data = {"success" : True, "data" :{"message" : "Record Deleted Successfully"}}
        except Exception as e:
            context_data = {"success" : False, "errors" : {"message":str(e)}}    
        return Response(context_data)    


def student_list(request, template_name="student/student_list.html"):
    variables = {
        "page_title": "Student Details",
        "student_list": Student.objects.all()
    }
    # return render_to_response(template_name,
    #                           RequestContext(request, variables))

    return render(request, template_name, variables)

def student_form(request, id=None, instance=None):
    if id:
        instance = get_object_or_404(Student, pk=id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            if not id:
                messages.success(request, 'Saved successfully.')
            else:
                messages.success(request, ' updated.')
            return HttpResponseRedirect(reverse('student_list'))
        else:
            print form.errors
    else:
        form = StudentForm(instance=instance)
    variables = {"form": form,
                 "campaign": instance,
                 "page_title": "Student Form",
                 "cancel_url": reverse("student_add")}
    current_url = resolve(request.path_info).url_name
    print current_url,"current_url"
    if current_url == 'campaign_view':
        template_name = "student/student_view.html"
    else:
        template_name = "student/student_form.html"
    return render_to_response(template_name,
                              RequestContext(request, variables))

def student_delete(request, id=None):
    student = get_object_or_404(Student, pk=id)   
    student.delete()
    messages.success(request, '%s Student Deleted Successfully,' %(student))
    return HttpResponseRedirect(reverse('student_list'))    
