from django.contrib import admin
from .models import Room, Renter, Price, Transition, ServiceCharge,Problem,Payment


admin.site.register(Room)
admin.site.register(Renter)
admin.site.register(Price)
admin.site.register(Transition)
admin.site.register(ServiceCharge)
admin.site.register(Payment)
admin.site.register(Problem)
