from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializer import Friendserializer
from .models import Friends
# Create your views here.

class FriendsCreateApi(generics.CreateAPIView):
    queryset = Friends.objects.all()
    serializer_class = Friendserializer

class FriendsListApi(generics.ListAPIView):
    queryset = Friends.objects.all()
    serializer_class = Friendserializer

class FriendsUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Friends.objects.all()
    serializer_class = Friendserializer