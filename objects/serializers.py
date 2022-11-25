from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'
        depth = 3

class ObjectDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = LabObject
        fields = '__all__'
        depth = 3