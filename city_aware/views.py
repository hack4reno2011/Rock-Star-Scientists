# -*- coding: utf-8 -*
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from livereno.models import Venues, Events

def venue_page(request, venue_id = None):

    a = {}

    if venue_id:
        try:
            venue_id = int(venue_id)
        except ValueError:
            raise Http404
        
        venue = get_object_or_404(Venues, pk=venue_id)
        
        events = Events.objects.select_related(depth=1).filter(venue=venue).order_by('start_time')
        a['venue'] = venue
        a['events'] = events
        
        return render(request, 'venue_page.html', a)

    a['venues'] = Venues.objects.all()

    return render(request, 'venue_list.html', a)
