"""
Definition of urls for DjangoWebProject2.
"""

from django.urls import path
from django.contrib import admin
from MyApp1 import views


urlpatterns = [
    path ( 'about' , views. about) ,
    path ( 'contact', views. contact), 
    path('q',views.page, name ='page'),
    path('',views.index, name ='home'),
    path ( 'admin/', admin. site. urls), 
]
