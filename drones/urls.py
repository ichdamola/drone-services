from django.urls import path
from rest_framework import routers

from drones.views import *

router = routers.SimpleRouter()
router.register(r"register", DroneViewset, basename="drone_registration")