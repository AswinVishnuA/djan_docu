from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.hello,name='hello'), 
    path('pined',views.pins,name='pins'), 
    path('your-name/',views.get_name,name='yourname'),
    path('contact/',views.contact,name='contact')
          
]
