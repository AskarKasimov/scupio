from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
@login_required
def index(request):
    object = Object.objects.select_related().all()
    context = {
        'objects': object,
    }
    return render(request, 'objects/index.html', context)


@login_required
def labs_list(request):
    labs = Lab.objects.select_related().distinct()
    context = {
        'labs': labs,
    }
    return render(request, 'objects/labs_list.html', context)


@login_required
def object_detail(request, object_id):
    object = get_object_or_404(Object, pk=object_id)
    context = {
        'object': object,
        'tasks': object.lab_object.all(),
    }
    return render(request, 'objects/object_detail.html', context)


def sign_in(request):
    if not request.user.is_authenticated:
        return render(request, 'auth/sign_in.html')
    else:
        context = {
            "name": request.user.email

        }
        return render(request, 'auth/auth.html',context)


def sign_up(request):
    return render(request, 'auth/sign_up.html')


def try_sign_up(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    print(name, email, password)
    user = User.objects.create_user(username=email, email=email, password=password)
    user.save()
    return render(request, 'auth/sign_up.html')


def log_out(request):
    logout(request)
    return render(request, 'auth/sign_in.html')


def try_sign_in(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = authenticate(username=email, email=email, password= password)
    print(user)
    if user is not None:
        login(request, user)
        return render(request, 'auth/success_sign_in.html')
    else:
        return render(request, 'auth/fail_sign_in.html')


@login_required
def lab_detail(request, lab_id):
    lab = get_object_or_404(Lab, name=lab_id)
    print(lab)
    context = {
        'lab': lab
    }
    return render(request, 'objects/lab_detail.html', context)


@login_required
def lab_search(request):
    a = request.POST.get('search')
    lab = get_object_or_404(Lab, name=a)
    context = {
        'lab': lab
    }
    return render(request, 'objects/lab_detail.html', context)

@login_required
def search_result(request):


    a = request.POST.get('search')

    object = get_object_or_404(Object, name=a)
    print(3)
    print(object.lab_object.all()[0].object.rock_name)
    context = {
        'objects': object,
        'tasks': object.lab_object.all()
    }
    print(5)
    return render(request, 'objects/object_detail.html', context)

def research_list(request):
    return HttpResponseRedirect("/sign-in")

