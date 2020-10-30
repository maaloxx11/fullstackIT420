from rest_framework import serializers
from .models import Room, Renter, Price, Transition, ServiceCharge


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "room_id",
            "room_type",
            "electric_meter",
            "water_meter",
            "room_status",
        )


class RenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Renter
        fields = (
            "renter_id",
            "firstname",
            "lastname",
            "address",
            "telephone",
        )


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = (
            "id",
            "price_description",
            "price_num",
        )


class TransitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transition
        fields = (
            "id",
            "room_id",
            "renter_id",
            "move_in_date",
            "move_out_date",
            "telephone",
        )


class ServiceChargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCharge
        fields = (
            "id",
            "room_id",
            "add_date",
            "deadline_date",
            "total",
        )
