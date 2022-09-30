from django.urls import path,include
from app1.views import *
urlpatterns = [
    path('home/',home.as_view(),name='home')
]