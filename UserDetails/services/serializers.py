from rest_framework import serializers
from form.models import *
from jsonfield import JSONField


class UserCategorySerializers(serializers.Serializer):
    class Meta:
        model = UserCategory
        fields = __all__