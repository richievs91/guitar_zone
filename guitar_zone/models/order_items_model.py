from django.db import models
from . import order_model, guitar_model


class OrderItems(models.Model):
    guitar = models.ForeignKey(guitar_model.Guitar, on_delete=models.CASCADE)
    order = models.ForeignKey(order_model.GuitarZoneOrder, on_delete=models.CASCADE)