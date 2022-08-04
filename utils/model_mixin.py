from django.db import models
from django.utils.timezone import now


class BaseMixin(models.Model):
    created_on = models.DateTimeField(default=now)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
