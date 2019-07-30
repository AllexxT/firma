
from django.contrib import admin
from django.urls import path, include
from sklad.views import hello
urlpatterns = [
    path('', hello)
]
