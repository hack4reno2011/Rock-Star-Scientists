# -*- coding: utf-8 -*
from django.shortcuts import render

def staff_home(request):
    #TODO direct to template
    a = {}
    return render(request, 'staff/staff_home.html', a)
    
def view_event_categories(request):
    #TODO direct to template
    a = {}
    return render(request, 'staff/event_categories_main.html', a)
    
def view_venues(request):
    #TODO direct to template
    a = {}
    return render(request, 'staff/venues_main.html', a)
