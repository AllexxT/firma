from .models import Trotuarka, Zabor, Materials
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.views import APIView


def hello(request):
    return HttpResponse("<h1 style='text-align:center'>Hello!</h1>")

#Rest framework

from rest_framework import viewsets
from .serializers import TroruarkaSerializer, ZaborSerializer, ZaborPostSerializer
from django.shortcuts import get_object_or_404

from django.views.decorators.csrf import csrf_exempt

class TrotuarkaViewSet(APIView):
    # queryset = Trotuarka.objects.all()
    # serializer_class = TroruarkaSerializer
    def get(self, request):
        if request.GET:
            trotuarka = Trotuarka.objects.all()
            serializer = TroruarkaSerializer(trotuarka, many=True)
            return Response(serializer.data)
        else:
            trot = Trotuarka.objects.all()
            serializer = TroruarkaSerializer(trot, many=True)
            return Response(serializer.data)    


# class ZaborViewSet(viewsets.ModelViewSet):

#     queryset = Zabor.objects.all()
#     serializer_class = ZaborSerializer


# class ZaborViewSet(APIView):

#     def get(self, request):
#         zabors = Zabor.objects.all()
#         serializer = ZaborSerializer(zabors, many=True)
#         return Response(serializer.data)


class ZaborView(APIView):

    def get(self, request):
        if request.GET:
            zabor = Zabor.objects.all()
            serializer = ZaborSerializer(zabor, many=True)
            return Response(serializer.data)
        else:
            zab = Zabor.objects.all()
            serializer = ZaborSerializer(zab, many=True)
            return Response(serializer.data)


    def post(self, request):
        serializer = ZaborPostSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'zabor is added', 'dt':serializer.data})
        else:
            return Response(serializer.errors)


# bt = Zabor.objects.get(name='but')
# print(bt.price)
# bt.price = 187
# bt.save()