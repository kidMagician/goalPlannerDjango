from django.urls import path,include
from .views import *

urlpatterns = [
    path(r'signup',signup.as_view(),name="signup"),
    path(r'signin',signin.as_view(),name="signin"),
    path(r'findpass',findpass.as_view(),name="findpass"),
]