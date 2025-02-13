from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("select_friend",views.select_friend ),
]