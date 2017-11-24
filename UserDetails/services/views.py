from django.shortcuts import render
from form.models import *
from services.serializers import *
from rest_framework.response import Response

# Create your views here.

def userlist(request):
    if request.method == "GET":
        user_obj = UserCategory.objects.all()
        #serilaizer = UserCategorySerializers(user_obj,many=True)
        return Response({"msg":"hi"})