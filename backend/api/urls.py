from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import (
    RoomViewSet,
    RenterViewSet,
    PriceViewSet,
    TransitionViewSet,
    ServiceChargeViewSet,
)

router = routers.DefaultRouter()
router.register("room", RoomViewSet)
router.register("renter", RenterViewSet)
router.register("price", PriceViewSet)
router.register("transition", TransitionViewSet)
router.register("servicecharge", ServiceChargeViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
