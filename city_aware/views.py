# -*- coding: utf-8 -*
from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from livereno.models import Venues, Events, Sponsors, EventCategories

def venue_page(request, venue_id = None):

    a = {}
    if venue_id:
        try:
            venue_id = int(venue_id)
        except ValueError:
            raise Http404
        
        venue = get_object_or_404(Venues, pk=venue_id)
        
        events = Events.objects.select_related(depth=1).filter(venue=venue, start_time__gte=datetime.now()).order_by('start_time')
        a['venue'] = venue
        a['events'] = events
        
        return render(request, 'venue_page.html', a)

    a['venues'] = Venues.objects.all()
    return render(request, 'venue_list.html', a)


def sponsor_page(request, sponsor_id = None):

    a = {}
    if sponsor_id:
        try:
            sponsor_id = int(sponsor_id)
        except ValueError:
            raise Http404
        
        sponsor = get_object_or_404(Sponsors, pk=sponsor_id)
        
        events = Events.objects.select_related(depth=1).filter(sponsor=sponsor, start_time__gte=datetime.now()).order_by('start_time')
        a['sponsor'] = sponsor
        a['events'] = events
        
        return render(request, 'sponsor_page.html', a)

    a['sponsors'] = Sponsors.objects.all()
    return render(request, 'sponsor_list.html', a)

def category_page(request, category_id = None):

    a = {}
    if category_id:
        try:
            category_id = int(category_id)
        except ValueError:
            raise Http404
        
        category = get_object_or_404(EventCategories, pk=category_id)
        
        events = Events.objects.select_related(depth=1).filter(category=category, start_time__gte=datetime.now()).order_by('start_time')
        #.extra(select={'is_recent': "start_date > {0}".format(datetime.now())})
        a['category'] = category
        a['events'] = events
        
        return render(request, 'category_page.html', a)

    a['categories'] = EventCategories.objects.all()
    return render(request, 'category_list.html', a)

def event_page(request, event_id = None):

    a = {}
    if event_id:
        try:
            event_id = int(event_id)
        except ValueError:
            raise Http404
        
        event = get_object_or_404(Events, pk=event_id)
        
        a['event'] = event
        return render(request, 'event_page.html', a)

    a['events'] = Events.objects.select_related(depth=1).all().order_by('start_time')
    return render(request, 'event_list.html', a)
