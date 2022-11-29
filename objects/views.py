from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponseRedirect



def index(request):
    object = Object.objects.select_related().all()
    context = {
        'objects': object,
    }
    return render(request, 'objects/index.html', context)

def labs_list(request):
    labs = Lab.objects.select_related().distinct()
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


def sign_in(request):
    return render(request, 'auth/sign_in.html')

def sign_up(request):
    return render(request, 'auth/sign_up.html')

def search_result(request):
    search_query = request.GET.get('search', '')
    if search_query:
        objects = Object.objects.filter(name__icontains=search_query)
    else:
        objects = Object.objects.all()

    context = {
        'objects': object,
    }
    return render(request, 'objects/index.html', context)

def research_list(request):
    return HttpResponseRedirect("/sign-in")

