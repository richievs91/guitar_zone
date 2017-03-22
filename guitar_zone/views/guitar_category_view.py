from django.contrib.auth.models import User, Group
from django.views import generic
from django.shortcuts import render
from django.views.generic.base import TemplateView
import sys
sys.path.append("../")
from guitar_zone.models.guitar_model import Guitar
from guitar_zone.models.guitar_type_model import GuitarType


def get_guitar_type_info(request, pk):
    guitar_type = GuitarType.objects.filter(id=pk)
    guitars = Guitar.objects.filter(guitar_type=pk)
    return render(request, 'guitar_zone/guitar_category.html', {
        'guitar_list': guitars,
        'guitar_type': guitar_type[0]
            })