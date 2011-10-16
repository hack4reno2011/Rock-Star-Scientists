from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization

from models import RawAddresses

class RawAddressResource(ModelResource):
    class Meta:
        filtering = {
            'latitude': ALL,
            'longitude': ALL,
            'longform': ALL,
            'municipality': ALL,
            #ALL ->  startswith, exact, lte, etc...
        }
        queryset = RawAddresses.objects.all()
        authentication = Authentication()
        authorization = Authorization()
