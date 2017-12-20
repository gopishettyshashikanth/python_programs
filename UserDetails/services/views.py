from django.shortcuts import render
from postform.models import *
from django.http import HttpResponse
from services.serializers import UserCategorySerializers,CheckMobileNumberSerializer,UserDeptSerializers

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
import json
from django.core import serializers
from django.http import Http404, JsonResponse
from postform.views import check_mobile_number 


@api_view(['GET'])
def userlist(request):
    if request.method == "GET":
        user_obj = UserCategory.objects.all()
        serializer = UserCategorySerializers(user_obj,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def deptlist(request):
    if request.method == 'GET':
        dept_obj = UserCategory.objects.filter(deptID=1)
        #dept_obj = UserCategory.objects.filter(name__contains = 'S')
        serializer = UserDeptSerializers(dept_obj,many=True)
        return Response(serializer.data)        

@api_view(['POST'])
def checkMobilenumber(request):
    if request.method == "POST":
        
        serializer = CheckMobileNumberSerializer(data=request.data)
        
        if serializer.is_valid():
            user_mobile = check_mobile_number(request.data['phone_number'])
            if user_mobile:
                return Response({"msg":"mobile number already exist"},status=200)
            else:
                return Response({"msg":"mobile number is valid"},status=200)
        else:
            return Response(serializer.errors)
    return Response(serializer.data)
        