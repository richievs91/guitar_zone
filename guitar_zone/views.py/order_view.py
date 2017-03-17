from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.views import generic
from django.views.generic.base import TemplateView
import sqlite3
import sys
sys.path.append("../")
from guitar_zone.models import order_model, payment_type_model
from collections import Counter

class BangazonOrderView(TemplateView):
    template_name = 'guitar_zone/templates/order.html'

def get_guitars_in_cart(request):
    """
    Returns Orders in a list form
    """
    print('This is the request for user', request.user.id)
    # <--- This gets order related to logged in Customer
    active_order = order_model.GuitarZoneOrder.objects.get(customer__user = request.user)

    # <--- Gets all products on the active order
    guitar_on_order = active_order.guitar.all()
    print("This is the first product: ", guitar_on_order[0].name)

    # <--- var to hold total price
    total_price = 0
    for guitar in guitar_on_order:
        total_price += guitar.price

    # <--- Create and update array for products on order with name, quantity and total price/item
    product_array = []
    prod = Counter(guitar_on_order)
    for p, q in prod.items():
        product_array.append((p.name, q, p.price * q))

    # <--- payment method
    payment_types = payment_type_model.PaymentType.objects.filter(customer__user = request.user)

    return render(request, 'guitar_zone/order.html', {"product": product_array, "total": total_price, "payment_types": payment_types})