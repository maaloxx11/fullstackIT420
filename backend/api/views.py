from django.shortcuts import render
from rest_framework import viewsets
from .models import Room, Renter, Price, Transition
from .serializers import RoomSerializer, RenterSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
    
class RenterViewSet(viewsets.ModelViewSet):
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer