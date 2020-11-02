from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import viewsets, status
from django_filters import rest_framework as filters
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


class TransitionFilter(filters.FilterSet):
    room_id = django_filters.NumberFilter(field_name="room_id")
    renter_id = django_filters.NumberFilter(field_name="renter_id")
    move_out_date = filters.BooleanFilter(
        field_name="move_out_date", lookup_expr="isnull"
    )

    class Meta:
        model = Transition
        fields = []


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ["room_type", "room_status"]

    @action(detail=True, methods=["POST"])
    def addservicecharge(self, request, pk=None):
        room = Room.objects.get(room_id=pk)
        ele = room.electric_meter_new
        water = room.water_meter_new
        total = ServiceCharge.objects.get(room_id=room.room_id)
        rates = Price.objects.all()
        for rate in rates:
            if rate.price_id == str(room.room_status):
                break
            rate_room = rate.price_num
        ele_rate = Price.objects.get(price_id="electric_rate")
        water_rate = Price.objects.get(price_id="water_rate")
        total.total = rate_room + (
            (ele_rate.price_num * ele) + (water_rate.price_num * water)
        )
        total.save()
        response = {total.total}
        serializer = ServiceChargeSerializer(total)
        return Response(response, status=status.HTTP_200_OK)


class RenterViewSet(viewsets.ModelViewSet):
    queryset = Renter.objects.all()
    serializer_class = RenterSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ["price_num", "price_id"]


class TransitionViewSet(viewsets.ModelViewSet):
    queryset = Transition.objects.all()
    serializer_class = TransitionSerializer
    filterset_class = TransitionFilter


class ServiceChargeViewSet(viewsets.ModelViewSet):
    queryset = ServiceCharge.objects.all()
    serializer_class = ServiceChargeSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ["room_id", "payment_status"]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer


def pri(request, price_num):
    queryset = Price.objects.filter(price_num=price_num)
    serializer_class = PriceSerializer
    return render(serializer_class.data)
