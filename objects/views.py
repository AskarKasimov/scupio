from django.shortcuts import render, get_object_or_404
from .models import *
from rest_framework import generics
from . import serializers
from rest_framework.decorators import api_view


def index(request):
    object = Object.objects.select_related().all()
    context = {
        'objects': object,
    }
    return render(request, 'objects/index.html', context)

def labs_list(request):
    labs = Lab.objects.select_related().all()
    context = {
        'labs': labs,
    }
    return render(request, 'objects/labs_list.html', context)

def object_detail(request, object_id):
    object = get_object_or_404(Object, pk=object_id)
    context = {
        'object': object,
        'tasks': object.lab_object.all(),
    }
    return render(request, 'objects/object_detail.html', context)


class ObjectList(generics.ListAPIView):
    queryset = Object.objects.all()
    serializer_class = serializers.ObjectSerializer


class ObjectDetail(generics.ListAPIView):
    queryset = LabObject.objects.all()
    serializer_class = serializers.ObjectDetailSerializer

def sign_in(request):
    return render(request, 'auth/sign_in.html')

def sign_up(request):
    return render(request, 'auth/sign_up.html')
