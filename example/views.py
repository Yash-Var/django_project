
from django.shortcuts import render
from random import randint
from django.http import JsonResponse
from rest_framework import viewsets

from example.serializers import PersonSerializer, SpeciesSerializer
from example.models import Like, Dislike
# Create your views here.
count=0
def index(request):
    if request.headers.get('X-Requested-With')=='XMLHttpRequest':
        number= randint(1,10)
        return JsonResponse({'number':number})
    return render(request,'example/index.html')


class PersonViewSet(viewsets.ModelViewSet):
   queryset = Like.objects.all()
   serializer_class = PersonSerializer


class SpeciesViewSet(viewsets.ModelViewSet):
   queryset = Dislike.objects.all()
   serializer_class = SpeciesSerializer

