from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',

    url(r'^/$', 'staff.views.staff_home', name='staff_home'),
)
