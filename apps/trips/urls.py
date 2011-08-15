from django.conf.urls.defaults import *

from trips.models import Trip, TripAdmin

urlpatterns = patterns('trips.views',
	#url('^create/$', 'create', name='trip_create'),
	url('^create/$', 'alt_create', name='alt_create'),
	url('^view/(?P<trip_id>\d+)/$', 'view', name='trip_view'),
	url('^list/(?P<user_id>\d+)/$', 'list', name='list'),
	url('^browse/$', 'browse', name='browse'),
)
