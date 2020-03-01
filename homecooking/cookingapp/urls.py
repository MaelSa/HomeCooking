from django.urls import path, include, reverse_lazy
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),

]