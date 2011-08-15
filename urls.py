from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
	(r'^trip/', include('trips.urls')),
	(r'^trips/', include('trips.urls')),
#	(r'^google_oauth/login/', 'google_oauth.views.login'),
#	(r'^google_oauth/get_token/', 'google_oauth.views.get_token'),
	(r'^registration/', include('registration.urls')),
	(r'^', include('index.urls')),
)

import os
from django.conf import settings
if settings.DEBUG:
	urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': os.path.join(os.path.dirname(__file__), 'static')}),
	)	
