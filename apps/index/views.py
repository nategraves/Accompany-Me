from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from trips.forms import IndexForm
from trips.models import TripAdmin

def home(request):
	form = IndexForm()
	if request.method == 'GET':
		render_to_response('trips/alt_create.html', {
			'where': request.POST['where'],
		}, context_instance=RequestContext(request))
	return render_to_response('index/index.html',{
		'form': form,
	}, context_instance=RequestContext(request))

@login_required
def user_home(request):
	trips = TripAdmin.objects.filter(user=request.user)
	return render_to_response('index/user_home.html',{
		'trips':trips,
}, context_instance=RequestContext(request))
