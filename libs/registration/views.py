from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.conf import settings


# I'm writing this method just in case I want to add additional, 
# user_profile kind of stuff later (e.g. FB info, prefs)
def register(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			# This redirect could either be to a user profile page or 
			# back to the trip created, if there is one in the session
			HttpResponseRedirect('/')
	return render_to_response('registration/register.html', {
		'form': form,
	}, context_instance=RequestContext(request))
