from rest_framework import serializers
from rest_api.models import *


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = {'name', 'email'}