# -*- coding: utf-8 -*
from django.shortcuts import render

from data.models import RawAddresses

def landing(request):
    a = {}
    return render(request, 'base.html', a)
    

def view_raw_addresses(request):

    a = {}
    a['items'] = RawAddresses.objects.all()

    return render(request, 'list.html', a)


def view_bone(request):
    
    a={}
    return render(request, 'backbone_ex.html', a)
    
def busstops_main(request):
    #TODO direct to template
    a={}
    return render(request, 'busstops_main.html', {})

def busstops_map(request):
    #TODO direct to template
    a={}
    return render(request, 'busstops_map.html', {})
