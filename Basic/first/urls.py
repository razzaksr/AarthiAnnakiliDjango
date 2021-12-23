from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.hai),
    path('info',views.hello),
    path('page',views.greet),
    path('data',views.send),
    path('log',views.verify)
]