from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('homepage', views.homepage),
    path('collections', views.collectionsPage),
    path('collections/<str:title>', views.singleCollection),
    # PROCESS
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    # TASK PROCESS
    path('createGeneralTask', views.createGenTask),
    path('createCollection', views.createCollection),
    path('deleteHomepageTask/<int:taskId>', views.deleteHomepageTask),
    path('collections/delete/<int:colId>', views.deleteCollection)
]