from rest_framework import serializers
from postform.models import *
from postform.views import *
from django.db.models import Q

class UserCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = UserCategory
        fields = '__all__'

class UserDeptSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserCategory
        fields = '__all__'          

class CheckMobileNumberSerializer(serializers.Serializer):
    
    phone_number = serializers.CharField(max_length=10)
        
    def validate_phone_number(self, value):
        if len(value) != 10:
            # if not value.isnumeric():
            #     raise serializers.ValidationError("Mobile Number Must Be Digits")
            raise serializers.ValidationError("Mobile Number Length Must Be 10 Digits")
        if not value.isnumeric():
            raise serializers.ValidationError("Mobile Number Must Be Digits")
        if not str(value).startswith(('2','7','8','9')):
            raise serializers.ValidationError("Invalid mobile number")
        return value

   
