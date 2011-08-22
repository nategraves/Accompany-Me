from django.conf.urls.defaults import *

from trips.models import Trip, TripAdmin

urlpatterns = patterns('trips.views',
	url('^browse/$', 'browse', name='browse'),
	url('^create/full/$', 'create', name='trip_create'),
	url('^create/$', 'create', name='trip_create'),
	url('^details/$', 'add_details', name='trip_details'),
	url('^invite/$', 'invite', name='invite'),
	url('^list/(?P<user_id>\d+)/$', 'list', name='list'),
	url('^view/(?P<trip_id>\w+)/$', 'view', name='trip_view'),
)
