from django.http import HttpResponse, HttpResponseRedirect
from .models import UserCategory
from .forms import userForm,signupForm
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404,render_to_response
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Template, Context, RequestContext

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Dept
from django.db.models import Avg, Max, Min, Sum

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

@login_required
def user_list(request,
                      template_name="forms/user_view_detail.html", search=None):
    no_of_rows = 0
    total_salary = 0
    if "search" in request.GET:
        search = request.GET.get('search').strip()
        user_list = UserCategory.objects.filter(name__contains=search).order_by('-name')
        total_salary = UserCategory.objects.filter(name=search).aggregate(Sum('salary'))
        no_of_rows = user_list.count()
    else:
        user_list = UserCategory.objects.all().order_by('-name')
        no_of_rows = user_list.count()
        total_salary = UserCategory.objects.all().aggregate(Sum('salary'))

    dept_table = []
    for each_dept in Dept.objects.all() :
        dept_list = UserCategory.objects.filter(deptID=each_dept)
        each_dict = {
        "name" : each_dept.deptName,
        "No_of_Emp" : dept_list.count(),
        "min_sal" : dept_list.aggregate(Min('salary'))['salary__min'],
        "max_sal" : dept_list.aggregate(Max('salary'))['salary__max'],
        "sum_sal" : dept_list.aggregate(Sum('salary'))['salary__sum']
        }
        dept_table.append(each_dict)
    #usercategory_list = UserCategory.objects.all()
    variables = {
        "page_title": "User Categories",
        "usercategory_list": user_list,
        "search" : search,
        "no_of_rows": no_of_rows,
        "total_salary" : total_salary['salary__sum'],
        "dept_table" : dept_table 
    }
    return render(request, 'forms/user_view_detail.html', variables)                           

def signup(request):

    if request.POST == "POST":

        form = signupForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('signup')
        else:    
            print form.errors
    else:
        form = signupForm()
    return render(request,'forms/signup.html',{'form': form})    
    
@login_required
def user_add(request):
    variables={}
    if request.method == "POST":
        #print request.POST
        form = userForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.tds=int(request.POST.get('salary'))*0.1
            post.save()            
            return redirect('user_list')
        else:
            print form.errors

    else:
        form = userForm()
    return render(request, 'forms/user_list.html', {'form': form})
@login_required         
def user_edit(request, pk=None):
    post = get_object_or_404(UserCategory, pk=pk)
    if request.method == "POST":
        form = userForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.tds=int(request.POST.get('salary'))*0.1
            post.save()
            template_name="forms/user_view_detail.html"

            dept_table = []
            for each_dept in Dept.objects.all() :
                dept_list = UserCategory.objects.filter(deptID=each_dept)
                each_dict = {
                "name" : each_dept.deptName,
                "No_of_Emp" : dept_list.count(),
                "min_sal" : dept_list.aggregate(Min('salary'))['salary__min'],
                "max_sal" : dept_list.aggregate(Max('salary'))['salary__max'],
                "sum_sal" : dept_list.aggregate(Sum('salary'))['salary__sum']
                }
                dept_table.append(each_dict)
            variables = {
            "usercategory_list": UserCategory.objects.all(),
            "dept_table" : dept_table 
            }
            return render_to_response(template_name,
                              RequestContext(request, variables))   
    else:
        form = userForm(instance=post)
        return render(request, 'forms/user_edit.html', {'form': form})


def user_view_detail(request, pk):
    post = get_object_or_404(UserCategory, pk=pk)
    return render(request, 'forms/user_view_detail.html', {'post': post}) 


def user_delete(request, id=None):
    server = get_object_or_404(UserCategory, pk=id) 
    server.delete()
    messages.success(request, 'Deleted Successfully,' )
    return HttpResponseRedirect(reverse('user_list'))
    
def user_search(request):

    if request.method == "GET":
        search = request.GET.get("search")
        user_list = UserCategory.objects.filter(name=search)
        return render(request, 'forms/user_view_detail.html', {'usercategory_list': user_list}) 

def index(request):
    user_list = UserCategory.objects.all()
    return render(request,'forms/home.html')
    #return HttpResponse("You must need to login")

def check_mobile_number(phone_number):
   
    flag = False
    try:
        user_obj = UserCategory.objects.get(phone_number=phone_number)
        if user_obj:
            flag = True
        else:
            flag = False
    except UserCategory.DoesNotExist as e:
        pass
    return flag


    

