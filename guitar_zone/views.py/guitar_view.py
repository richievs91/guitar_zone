from django.contrib.auth.models import User, Group
from django.views import generic
from django.shortcuts import render
from django.views.generic.base import TemplateView
import sys
sys.path.append("../")
from guitar_zone.models import guitar_model, guitar_type_model


def get_guitars_types_and_count(request):
    guitar_type_queryset = guitar_type_model.GuitarType.objects.all()
    g_queryset = []

    for gt in guitar_type_queryset:
        g = guitar_model.Guitar.objects.filter(guitar_type=gt.pk).order_by('pub_date')

        guitar_type_info = {
            'type_id': gt.pk, 
            'type_label_name': gt.label_name,
            'g_list': g.reverse()[:20],
            'count': g.count()
        }

        g_queryset.append(guitar_type_info)
        print("PLIST:", guitar_type_info['g_list'])

    # print("PRODUCT QUERYSET", p_queryset)

    return render(request, 'guitar_zone/guitars.html', {
        'guitars_info': g_queryset
    })
