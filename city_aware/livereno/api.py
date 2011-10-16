from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization

from models import Venues, Sponsors, EventCategories, Events

#TODO relations!
class VenuesResource(ModelResource):
    class Meta:
        filtering = {
            'latitude': ALL,
            'longitude': ALL,
            'name': ALL,
        }
        limit = 50
        queryset = Venues.objects.all()
        authentication = Authentication()
        authorization = Authorization()


class SponsorsResource(ModelResource):
    venue = fields.ForeignKey(VenuesResource, 'venue', null=True)
    class Meta:
        filtering = {
            'name': ALL,
        }
        limit = 50
        queryset = Sponsors.objects.all()
        authentication = Authentication()
        authorization = Authorization()


class EventsResource(ModelResource):
    venue = fields.ForeignKey(VenuesResource, 'venue', full=True)
    class Meta:
        filtering = {
            'name': ALL,
            'start_time': ALL,
            'end_time': ALL,
        }
        limit = 100
        queryset = Events.objects.all()
        authentication = Authentication()
        authorization = Authorization()
        

class EventCategoriesResource(ModelResource):
    class Meta:
        filtering = {
            'name': ALL,
        }
        limit = 50
        queryset = EventCategories.objects.all()
        authentication = Authentication()
        authorization = Authorization()

