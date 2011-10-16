# -*- coding: utf-8 -*
from django.shortcuts import render

def staff_home(request):
    #TODO direct to template
    a = {}
    return render(request, 'staff/staff_home.html', a)
