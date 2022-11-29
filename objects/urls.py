from django.urls import path
from . import views

from django.urls import path

urlpatterns = [
    path('', views.index),
    path('labs/', views.labs_list),
    path('object/<int:object_id>', views.object_detail, name='object_detail'),
    path('sign-in', views.sign_in),
    path('sign-up', views.sign_up),
    path('researches', views.research_list),
]