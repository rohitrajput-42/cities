from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "homepage"),
    path('addcity/', views.addcity, name = "addcity"),
    path('city/', views.city, name = "city"),
]