from django.conf.urls.defaults import *

from trips.models import Trip, TripAdmin

urlpatterns = patterns('trips.views',
	#url('^create/$', 'create', name='trip_create'),
	url('^create/$', 'alt_create', name='trip_create'),
	url('^details/$', 'add_details', name='trip_details'),
	url('^view/(?P<trip_id>\w+)/$', 'view', name='trip_view'),
	url('^list/(?P<user_id>\d+)/$', 'list', name='list'),
	url('^browse/$', 'browse', name='browse'),
)
