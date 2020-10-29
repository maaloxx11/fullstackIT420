from django.contrib import admin
from .models import Room, Renter, Price, Transition


admin.site.register(Room)
admin.site.register(Renter)
admin.site.register(Price)
admin.site.register(Transition)
