from django import forms
from guitar_zone.models.payment_type_model import PaymentType
from guitar_zone.models.guitar_model import Guitar
from django.utils.translation import ugettext_lazy as _

class PaymentTypeForm(forms.ModelForm):

    class Meta:
        model = PaymentType
        help_texts = {
            'card_type': _('Card Type:'),
            'card_number': _('Card Number:'),
            'cvv': _('3 digit cvv '),
            'expiration': _('Exp. Date:'),
            'name_on_card': _('Full Name on Card:')
        }
        fields = ('card_type', 'card_number', 'cvv', 'expiration', 'name_on_card')

class RentOutGuitarForm(forms.ModelForm):

    class Meta:
        model = Guitar
        help_texts = {
            'name': _('Guitar Make/Model:'),
            'description': _('Description:'),
            'price': _('Price/hr:'),
            'guitar_type': _('Choose Category:')
        }
        fields = ('name', 'description', 'price', 'guitar_type')