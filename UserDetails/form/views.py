from django.http import HttpResponse, HttpResponseRedirect
from .models import UserCategory
from .forms import userForm
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404,render_to_response
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Template, Context, RequestContext
from django.db.models import Sum

from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Avg, Max, Min, Sum

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

    for i in range(3):
        
        max_salary = UserCategory.objects.filter(deptID=i+1).aggregate(Max('salary'))
        min_salary = UserCategory.objects.filter(deptID=i+1).aggregate(Min('salary'))   
        print i+1
        # print max_salary['salary__max']
        # print min_salary['salary__min']
        max_salary_list = max_salary['salary__max']
        min_salary_list = min_salary['salary__min']
        print max_salary_list
        print min_salary_list

    # max_salary = UserCategory.objects.filter(deptID=3).aggregate(Max('salary'))
    # min_salary = UserCategory.objects.filter(deptID=3).aggregate(Min('salary'))   
    #print max_salary['salary__max']

    page = request.GET.get('page', 1)    
    paginator = Paginator(user_list, 10)
    
    try:
        usercategory_list = paginator.page(page)
    except PageNotAnInteger:
        usercategory_list = paginator.page(1)
    except EmptyPage:
        usercategory_list = paginator.page(paginator.num_pages) 
    
    variables = {
        "page_title": "User Categories",
        "usercategory_list": usercategory_list,
        "search" : search,
        "no_of_rows": no_of_rows,
        "total_salary" : total_salary['salary__sum'],
        "max_salary" : max_salary_list,
        "min_salary" : min_salary_list
    }
    return render(request, 'forms/user_view_detail.html', variables)                           

def user_add(request, template_name='forms/user_view_detail.html'):
    variables={}
    if request.method == "POST":
        form = userForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.tds=int(request.POST.get('salary'))*0.1
            post.save()
            return HttpResponseRedirect(reverse('user_list'))
        else:
            print form.errors
    else:
        form = userForm()
        return render(request, 'forms/user_list.html', {'form': form})
            
def user_edit(request, pk=None):
    post = get_object_or_404(UserCategory, pk=pk)
    print request.method
    if request.method == "POST":
        form = userForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.tds=int(request.POST.get('salary'))*0.1
            post.save()
            template_name="forms/user_view_detail.html"
            variables = {

            "usercategory_list": UserCategory.objects.all()
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
    page = request.GET.get('page', 1)    
    paginator = Paginator(user_list, 10)
    
    try:
        usercategory_list = paginator.page(page)
    except PageNotAnInteger:
        usercategory_list = paginator.page(1)
    except EmptyPage:
        usercategory_list = paginator.page(paginator.num_pages) 
    return render(request, 'forms/user_view_detail.html', { 'usercategory_list': usercategory_list })

