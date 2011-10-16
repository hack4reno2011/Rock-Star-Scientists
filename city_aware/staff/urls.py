from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',

    url(r'^/$', 'staff.views.staff_home', name='staff_home'),
    url(r'^/event-categories$', 'staff.views.view_event_categories', name='view_event_categories'),
    url(r'^/venues$', 'staff.views.view_venues', name='view_venues'),
)
