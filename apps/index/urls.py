from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('index.views',
	url(r'^$', 'home', name='home'),
	url(r'member/$', 'user_home', name='user_home'),
)
