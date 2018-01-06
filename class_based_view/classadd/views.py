from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


class getinput(View):
	def get(self,request):
		return render(request,'getinput.html')


class postinput(View):
	def get(self,request):
		return render(request,'postinput.html')

class add(View):
	def get(self,request):
		a=request.GET['t1']
		x=int(a)
		b=request.GET['t2']		
		y=int(b)

		z=str(x+y)
		return HttpResponse(z)

	def post(self,request):
		a=request.POST['t1']
		x=int(a)
		b=request.POST['t2']		
		y=int(b)

		z=str(x+y)
		return HttpResponse(z)



