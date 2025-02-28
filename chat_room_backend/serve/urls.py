from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("select_friend",views.select_friend ),
    path("get_history",views.get_history ),
    path("get_group_history",views.get_group_history ),
    path("login",views.login),
    path("append_history",views.append_history),
    path("append_group_history",views.append_group_history),
    path("get_private_info",views.get_private_info),
    path("add_friend",views.add_friend),
    path("check_friend_request",views.check_friend_request),
    path("accept_friend_request",views.accept_friend_request),

]