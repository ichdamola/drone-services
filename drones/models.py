from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from utils.model_mixin import BaseMixin
from drones.dependencies.choices import *

# Create your models here.
class Drone(BaseMixin):
    serial_number = models.CharField(max_length=100)
    model = models.CharField(max_length=30, choices=MODELS, unique=True,)
    weight = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    battery_capacity = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    state = models.CharField(max_length=30, choices=STATES, unique=True,)

    class Meta:
        verbose_name_plural = "Drones"

    def __str__(self):
        return f"{self.serial_number}"
