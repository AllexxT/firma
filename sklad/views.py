from django.shortcuts import render
from django.http import HttpResponse
from .models import Trotuarka, Zabor, Materials
# Create your views here.

def hello(request):
    return HttpResponse("Hello")

#Rest framework

from rest_framework import viewsets
from .serializers import TroruarkaSerializer, ZaborSerializer

class TrotuarkaViewSet(viewsets.ModelViewSet):
    queryset = Trotuarka.objects.all()
    serializer_class = TroruarkaSerializer


class ZaborViewSet(viewsets.ModelViewSet):
    queryset = Zabor.objects.all()
    serializer_class = ZaborSerializer