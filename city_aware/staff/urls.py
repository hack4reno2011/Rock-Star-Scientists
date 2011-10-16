from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',

    url(r'^/$', 'staff.views.staff_home', name='staff_home'),
    url(r'^/event-categories$', 'staff.views.view_event_categories', name='view_event_categories'),
    url(r'^/venues$', 'staff.views.view_venues', name='view_venues'),
    url(r'^/sponsors$', 'staff.views.edit_sponsors', name='edit_sponsors'),
    
    url(r'^/list-sponsors$', 'staff.views.list_sponsors', name='list_sponsors'),
    url(r'^/list-venues$', 'staff.views.list_venues', name='list_venues'),
    url(r'^/list-categories$', 'staff.views.list_categories', name='list_categories'),
    url(r'^/list-events$', 'staff.views.list_events', name='list_events'),
)
