from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Room, Renter, Price, Transition, ServiceCharge, Payment, Problem
from .serializers import (
    RoomSerializer,
    RenterSerializer,
    PriceSerializer,
    TransitionSerializer,
    ServiceChargeSerializer,
    PaymentSerializer,
    ProblemSerializer,
)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    """ @action(detail=True, methods=["POST"])
    def addservicecharge(self, request, pk=None):
        room = Room.objects.get(room_id=pk)
        ele = room.electric_meter
        water = room.water_meter
        total = ServiceCharge.objects.get(room_id=room.room_id)
        total.total = ele+water
        total.save()
        response = {ele+water}
        serializer = ServiceChargeSerializer(total,many= False )
        return Response(response, status=status.HTTP_200_OK)
 """


class RenterViewSet(viewsets.ModelViewSet):
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class TransitionViewSet(viewsets.ModelViewSet):
    queryset = Transition.objects.all()
    serializer_class = TransitionSerializer


class ServiceChargeViewSet(viewsets.ModelViewSet):
    queryset = ServiceCharge.objects.all()
    serializer_class = ServiceChargeSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer