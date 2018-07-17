from django.urls import path,include
from .views import *

urlpatterns = [

    path(r'goal',goal.as_view(),name="goal"),
    path(r'task',task.as_view(),name="createtask"),
]