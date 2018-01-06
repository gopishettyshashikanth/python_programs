from django.shortcuts import render
from django.http import HttpResponse

def input(request):
    return render(request,'base.html')

def add(request):

    if request.method == "GET":

        try:
            a = request.GET['t1']
            x= int(a)
            b = request.GET['t2']
            y = int(b)

            z=x+y
            return HttpResponse(str(z))
        except(ValueError):
            return HttpResponse("invalid error")  

    else:

        try:
            a = request.POST['t1']
            x=int(a)
            b = request.POST['t2']           
            y=int(b)

            z = x+y
            return HttpResponse("<html><body><h1>sum is "+str(z)+"</h1></body></html>")

        except(ValueError):
            return HttpResponse("invalid input")    
        