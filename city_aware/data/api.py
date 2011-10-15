from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization

from models import RawAddresses

class RawAddressResource(ModelResource):
    class Meta:
        queryset = RawAddresses.objects.all()
        authentication = Authentication()
        authorization = Authorization()
