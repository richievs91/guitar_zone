from django.contrib.auth.models import User, Group
from django.views import generic
from django.shortcuts import render
from django.views.generic.base import TemplateView
import sys
sys.path.append("../")
from guitar_zone.models.guitar_model import Guitar
from guitar_zone.models.guitar_type_model import GuitarType


def get_product_type_info(request, pk):
    product_type = GuitarType.objects.filter(id=pk)
    products = Guitar.objects.filter(product_type=pk)
    return render(request, 'guitar_zone/guitar_category.html', {
        'product_list': products,
        'product_type': product_type[0]
            })