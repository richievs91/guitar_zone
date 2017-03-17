from django.db import models
from . import customer_model, payment_type_model, guitar_model

class GuitarZoneOrder(models.Model):
    """
    Stores a Rent Order
    Method List:
    -set_order_is_complete
    -get_order_is_complete
    -get_products_in_cart
    Argument List:
    -models.Model Allows the class to access field types
    """
    customer = models.ForeignKey(customer_model.Customer, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(payment_type_model.PaymentType, on_delete=models.CASCADE, null = True)
    order_is_complete = models.BooleanField()
    guitar = models.ManyToManyField(guitar_model.Guitar, through = 'OrderItems')

    def set_order_is_complete(self):
        self.order_is_complete = 1
        return self.order_is_complete

    def get_order_is_complete(self):
        return self.order_is_complete