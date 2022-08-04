from rest_framework import serializers

from drones.models import *


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = "__all__"
        read_only_fields = ["id",]