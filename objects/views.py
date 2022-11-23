from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    object = Object.objects.select_related().all()
    context = {
        'subjects': object,
    }
    return render(request, 'objects/index.html', context)