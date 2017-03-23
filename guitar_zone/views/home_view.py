from django.contrib.auth.models import User, Group 
from django.views import generic
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.db.models import Q
import sys
sys.path.append("../")
from guitar_zone.models import guitar_model, guitar_type_model


def get_guitars_and_types(request):
    guitar_type_queryset = guitar_type_model.GuitarType.objects.all()
    guitar_queryset = []

    for gt in guitar_type_queryset:
        g = guitar_model.Guitar.objects.filter(guitar_type=gt.pk).order_by('pub_date').reverse()[:2]
        guitar_queryset.append(g)


    return render(request, 'guitar_zone/home.html', {
        'guitar':guitar_queryset,
        'guitar_type':guitar_type_queryset
    })