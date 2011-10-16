from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from data.api import RawAddressResource, BusStopsResource
from livereno.api import VenuesResource, SponsorsResource, EventsResource, EventCategoriesResource

city_api = Api(api_name='api')
city_api.register(RawAddressResource())
city_api.register(BusStopsResource())

city_api.register(VenuesResource())
city_api.register(SponsorsResource())
city_api.register(EventsResource())
city_api.register(EventCategoriesResource())

urlpatterns = patterns('',

    url(r'^$', 'data.views.landing', name='landing'),
    url(r'^raw-addresses$', 'data.views.view_raw_addresses', name='view_raw_addresses'),
    
    url(r'^bone$', 'data.views.view_bone', name='backbone'),
    url(r'^busstops$', 'data.views.busstops_main', name='busstops'),
    url(r'^busmap$', 'data.views.busstops_map', name='busmap'),

    url(r'^venues(?:/(?P<venue_id>\d+))?$', 'views.venue_page', name='venue_page'),
    url(r'^events(?:/(?P<event_id>\d+))?$', 'views.event_page', name='event_page'),
    url(r'^sponsors(?:/(?P<sponsor_id>\d+))?$', 'views.sponsor_page', name='sponsor_page'),
    url(r'^categories(?:/(?P<category_id>\d+))?$', 'views.category_page', name='category_page'),
    
    url(r'^', include(city_api.urls)),
    url(r'^staff', include('staff.urls')),

    # Examples:
    # url(r'^$', 'city_aware.views.home', name='home'),
    # url(r'^city_aware/', include('city_aware.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

#test with curl
#curl -H "Accept: application/json" http://127.0.0.1:8080/api/countries/
#curl -d "name=European%20Union&abbrev=EU" http://127.0.0.1:8080/api/regions/
#curl -F "fileupload=@filename.txt" http://example.com/resource.cgi
#curl --dump-header - -H "Content-Type: application/json" -X DELETE  http://localhost:8080/api/testdata/1/
#curl -H "Content-Type: application/json" -d "name=What" http://127.0.0.1:8080/api/testdata/
#curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"name": "What"}' http://localhost:8080/api/testdata/
#wget --header='Content-Type: application/json' --post-data '{"name": "ZOMG"}' http://localhost:8080/api/testdata/
