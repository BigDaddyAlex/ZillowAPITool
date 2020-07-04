
from django.urls import path, re_path
from . import views
from django.views.static import serve
import os

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('download/', views.downloadpage, name='downloadpage'),
    
]