from rest_framework.viewsets import ModelViewSet

from drones.serializers import *
from drones.models import *

# Create your views here.
class DroneViewset(ModelViewSet):
    """Register a drone."""
    
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    http_method_names = ["post"]