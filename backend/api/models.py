from django.db import models
import datetime    
from django.db.models.functions import TruncMonth
from django.db.models import Count,Func

class Room(models.Model):
    room_id = models.IntegerField(primary_key=True)
    room_type = models.IntegerField()
    electric_meter_old = models.IntegerField(blank=True,null=True)
    water_meter_old = models.IntegerField(blank=True,null=True)
    electric_meter_new = models.IntegerField(default=0)
    water_meter_new = models.IntegerField(default=0)
    room_status = models.IntegerField(default=1)


class Renter(models.Model):
    renter_id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    address = models.TextField(max_length=300)
    telephone = models.IntegerField()


class Price(models.Model):
    price_id = models.CharField(primary_key=True,max_length=20,default=0)
    price_description = models.CharField(max_length=30)
    price_num = models.IntegerField()


class Transition(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    renter_id = models.ForeignKey(Renter, on_delete=models.CASCADE)
    move_in_date = models.DateField(auto_now=False, auto_now_add=False,)
    move_out_date = models.DateField(auto_now=False, auto_now_add=False, blank=True,null=True)

class ServiceCharge(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    add_date = models.DateField(default=datetime.date.today, blank=True)
    deadline_date = models.DateField(auto_now=False, auto_now_add=False,blank=True,null=True)
    total = models.FloatField(default=0)
    price_electric_meter = models.IntegerField(blank=True,null=True)
    price_water_meter = models.IntegerField( blank=True,null=True)
    payment_status = models.IntegerField(default=1)
    status = models.IntegerField(default=1)


class Payment(models.Model):
    sc_id = models.ForeignKey(ServiceCharge, on_delete=models.CASCADE)
    total_payment = models.FloatField()
    payment_date = models.DateField(auto_now=False, auto_now_add=False)


class Problem(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    promblem_description = models.TextField(max_length=100)
    problem_date = models.DateField(auto_now=False, auto_now_add=False)


