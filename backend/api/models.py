from django.db import models


class Room(models.Model):
    room_id = models.IntegerField(primary_key=True)
    room_type = models.IntegerField()
    electric_meter = models.IntegerField()
    water_meter = models.IntegerField()
    room_status = models.IntegerField()


class Renter(models.Model):
    renter_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    address = models.TextField(max_length=300)
    telephone = models.IntegerField()


class Price(models.Model):
    price_description = models.CharField(max_length=20)
    price_num = models.IntegerField()


class Transition(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    renter_id = models.ForeignKey(Renter, on_delete=models.CASCADE)
    move_in_date = models.DateField(auto_now=False, auto_now_add=False)
    move_out_date = models.DateField(auto_now=False, auto_now_add=False, blank=True)
