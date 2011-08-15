from django.conf.urls.defaults import *
from django.contrib.auth.views import login as django_login
from django.contrib.auth.views import logout as django_logout

urlpatterns = patterns('registration.views',
	url('^login/$', django_login),
	url('^logout/$', django_logout),
	url('^register/$', 'register', name='user_register'),
)
