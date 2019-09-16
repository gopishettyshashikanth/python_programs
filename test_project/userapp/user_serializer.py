from rest_framework import serializers
from . import *


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    gender = serializers.CharField(max_length=30)
    dob = serializers.CharField(max_length=30)
   