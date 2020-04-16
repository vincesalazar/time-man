from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('homepage', views.homepage),
    path('addTask', views.addTask),
    # PROCESS
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    # TASK PROCESS
    path('createTask', views.createTask),
]