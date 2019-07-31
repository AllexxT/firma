
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'trotuarka', views.TrotuarkaViewSet)
router.register(r'zabor', views.ZaborViewSet)




urlpatterns = [
    path('', views.hello),
    re_path(r'^', include(router.urls))
]
