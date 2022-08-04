from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from utils.model_mixin import BaseMixin
from drones.dependencies.choices import *
from drones.dependencies.services import VALIDATE_CHARACTER

from cloudinary.models import CloudinaryField


# Create your models here.
class Medication(BaseMixin):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    code = models.CharField(max_length=100, validators=[VALIDATE_CHARACTER])
    image = CloudinaryField('image')

    class Meta:
        verbose_name_plural = "Medications"

    def __str__(self):
        return f"{self.serial_number}"


class Drone(BaseMixin):
    serial_number = models.CharField(max_length=100)
    model = models.CharField(max_length=30, choices=MODELS, unique=True)
    state = models.CharField(max_length=30, choices=STATES, unique=True)
    weight = models.IntegerField(
        default=1, 
        validators=[MaxValueValidator(100), 
        MinValueValidator(1)]
    )
    battery_capacity = models.IntegerField(
        default=0, 
        validators=[MaxValueValidator(100), 
        MinValueValidator(0)]
    )
    medication = models.ForeignKey(
        Medication,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name_plural = "Drones"

    def __str__(self):
        return f"{self.serial_number}"
