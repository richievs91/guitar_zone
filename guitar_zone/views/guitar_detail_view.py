from django.contrib.auth.models import User, Group
from django.views import generic
import sys
sys.path.append("../")
from guitar_zone.models import GuitarType, Guitar, GuitarZoneOrder, Customer, OrderItems
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login, authenticate
from guitar_zone import models


class GuitarDetailView(DetailView):
    model = Guitar

def get_guitar_detail(request):
    guitar_detail_view = Guitar.objects.filter(id=id)
    return render(request, 'guitar_zone/guitar_detail.html', {'guitar': guitar_detail_view})

def add_guitar_to_order(request, pk):
    print("REQUEST IS HERE:::::::::: ", request)
    guitar = Guitar.objects.get(id = pk)


    try:
        order_pk = GuitarZoneOrder.objects.get(customer = request.user.id)
        new_order = GuitarZoneOrder.objects.get(id = order_pk.id, order_is_complete = False)
    except:
        customer = Customer.objects.get(user = request.user)
        new_order = GuitarZoneOrder.objects.create(order_is_complete = False, customer = customer, payment_type = None)
        new_order.save()

    orderitem = models.OrderItems(guitar=guitar, order=new_order)
    orderitem.save()

    return HttpResponseRedirect(redirect_to='/guitar_zone/guitars/')
