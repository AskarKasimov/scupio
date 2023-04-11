from django.urls import path
from . import views

from django.urls import path

urlpatterns = [
    path('', views.sign_in),
    path('index', views.index),
    path("search_obj", views.search_result),

    path("labs/search_lab", views.lab_search),
    path('labs/', views.labs_list),
    path('object/<int:object_id>', views.object_detail, name='object_detail'),
    path('labs/<int:lab_id>', views.lab_detail, name='lab_detail'),
    path('sign-in', views.sign_in),
    path('sign-up', views.sign_up),
    path('log-out', views.log_out),
    path('try-sign-up', views.try_sign_up),
    path('try-sign-in', views.try_sign_in),
    path('researches', views.research_list),
]