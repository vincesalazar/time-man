from django.urls import path
from . import views

urlpatterns = [
    # TEMPLATES
    path('', views.index),
    path('homepage', views.homepage),
    path('collections', views.collectionsPage),
    path('collections/<str:title>', views.singleCollection),
    # LOGIN REG PROCESS
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    # TASK PROCESS
    path('homepage/createTask', views.createGenTask),
    path('createCollection', views.createCollection),
    path('createCollTask', views.createTaskForSingleCollection),
    path('delete/homepageTask/<int:taskId>', views.deleteHomepageTask),
    path('delete/singleColl/<int:collId>/<int:taskId>', views.deleteTaskFromSingleColl),
    path('delete/<int:colId>', views.deleteCollFromHome),
    path('collections/delete/<int:colId>', views.deleteCollFromColl),
]