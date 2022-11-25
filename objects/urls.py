from django.urls import path, include
from . import views

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index),
    path('labs/', views.labs_list),
    path('object/<int:object_id>', views.object_detail, name='object_detail'),
    path('sign-in', views.sign_in),
    path('sign-up', views.sign_up),
    path('researches', views.research_list),
    
    path('objects_api/', views.ObjectList.as_view()),
    path('object_api/<int:object_id>', views.ObjectDetail.as_view()),
]