from django.db import models
from guitar_zone.models.customer_model import Customer


class PaymentType(models.Model):

    """
    PaymentType model class
    The purpose of this class is to define a customer's payment types
    """

    card_type = models.CharField(max_length=30)
    card_number = models.CharField(max_length=25)
    cvv = models.CharField(max_length=4)
    expiration = models.DateField(auto_now=False)
    name_on_card = models.CharField(max_length=55)
    customer = models.ForeignKey(Customer, null=True)

    class Meta:
        verbose_name_plural = "PaymentTypes"

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.card_type, self.card_number, self.cvv, self.expiration, self.name_on_card, self.customer,)

    def get_name_on_card(self):
        return self.name_on_card

    def get_card_type(self):
        return self.card_type

    def get_card_number(self):
        return self.card_number

    def get_expiration(self):
        return self.expiration

    def get_cvv(self):
        return self.cvv

    def get_customer(self):
        return self.customer

    def get_customer_name(self):
        return self.customer.get_full_name()