from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings
import gdata.gauth
import gdata.contacts.client

from trips.models import Trip, TripAdmin, Why, Who
from trips.forms import IndexForm


CALLBACK_URL = 'http://localhost:8000/google_oath/get_token/'
SCOPES = ['https://www.google.com/m8/feeds/']

def google_login(request):
	client = gdata.contacts.client.ContactsClient(source='my website')
	request_token = client.GetOAuthToken(SCOPES, CALLBACK_URL, 
										settings.GOOGLE_CONSUMER_KEY,
										consumer_secret=settings.GOOGLE_CONSUMER_SECRET)
	request.session['google_request_token'] = request_token
	return HttpResponseRedirect(request_token.generate_authorization_url(domain=None))

def get_token(request):
	saved_token = request.session['google_request_token']
	request_token = gdata.gauth.AuthorizeRequestToken(saved_token, request.uri)
	query = gdata.contacts.client.ContactsQuery()
	query.updated_min = updated_min
	feed = gd_client.GetContacts(q = query)
	print feed

def view(request, trip_id):
	trip = get_object_or_404(Trip, pk=trip_id)
	who = Who.objects.filter(trip=trip)
	why = Why.objects.filter(trip=trip)
	return render_to_response('trips/view.html', {
		'trip': trip,
		'who': who,
		'why': why,
	}, context_instance=RequestContext(request))

