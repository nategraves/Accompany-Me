import logging
logger = logging.getLogger(__name__)

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from trips.models import Trip, TripAdmin, Why, Who
from trips.forms import IndexForm, AltIndexForm

def alt_create(request):
	if request.POST:
		form = AltIndexForm()
		if request.POST['where']:
			where = request.POST['where'] 
		else: 
			where = 'New York'
		return render_to_response('trips/alt_create.html', {
			'where': where,
			'form': form,
		}, context_instance=RequestContext(request))
	return HttpResponseRedirect('/')

def create(request):
	form = IndexForm()
	if request.method == 'POST':
		form = IndexForm(request.POST)
		if form.is_valid():
			# Create new trip first
			new_trip = Trip(where=request.POST['where'], when=request.POST.get('when'))
			new_trip.save()
			if request.user.is_authenticated():
				new_trip.author = request.user
				trip_admin = TripAdmin(new_trip, request.user)
			else:
				request.session['trip_id'] = new_trip.id 
			# Now add the why
			if request.POST.get('why'):
				new_why = Why(why=request.POST['why'], trip=new_trip)
				new_why.save()
			
			# Finish with the who
			if request.POST.get('who'):
				new_who = Who(who=request.POST['who'], trip=new_trip)
				new_who.save()
			
			# Give a nice message
			messages.success(request, 'Your trip has been created!')

			return HttpResponseRedirect('/trips/view/%d/' % new_trip.id)
	return render_to_response('trips/create.html', {
		'form': form,
	}, context_instance=RequestContext(request))

def create_when(request):
	pass

def create_why(request):
	pass

def create_who(request):
	pass

def view(request, trip_id):
	logger.error(trip_id)
	trip = get_object_or_404(Trip, mykey=trip_id)
	who = Who.objects.filter(trip=trip)
	why = Why.objects.filter(trip=trip)
	return render_to_response('trips/view.html', {
		'trip': trip,
		'who': who,
		'why': why,
	}, context_instance=RequestContext(request))

def list(request, user_id):
	trips = TripAdmin.objects.filter(user=user_id)
	return render_to_response('trips/list.html', {
		'trips': trips,
	}, context_instance=RequestContext(request))

def browse(request):
	trips = TripAdmin.objects.filter(trip__private=False)
	return render_to_response('trips/list.html', {
		'trips':trips,
	}, context_instance=RequestContext(request))
