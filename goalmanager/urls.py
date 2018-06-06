from django.urls import path,include
from .views import *

urlpatterns = [

    path(r'creategoal',createGoal.as_view(),name="creategoal"),
    path(r'getallgoals',getallGoal.as_view(),name="getallgoal"),
    path(r'createtask',createTask.as_view(),name="createtask")
]