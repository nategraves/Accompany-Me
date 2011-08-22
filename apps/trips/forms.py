from django import forms

from trips.models import Trip, Why, Who, Invite

class IndexForm(forms.Form):
	where = forms.CharField(widget=forms.TextInput(attrs={'class':'where alpha grid_13'}))

class DetailsForm(forms.Form):
	when = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'where'}))
	desc = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'where'}))

class TripForm(forms.ModelForm):
	when = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'alpha grid_16 where'}))
	where = forms.CharField(widget=forms.TextInput(attrs={'class':'alpha grid_16 where'}))
	class Meta:
		model = Trip
		fields = ('when', 'where',)

class WhyForm(forms.ModelForm):
	why = forms.CharField(widget=forms.TextInput(attrs={'class':'alpha grid_16 where'}))
	class Meta:
		model = Why
		fields = ('why',)

class WhoForm(forms.ModelForm):
	who = forms.CharField(widget=forms.TextInput(attrs={'class':'alpha grid_16 where'}))
	class Meta:
		model = Who
		fields = ('who',)

class InviteForm(forms.ModelForm):
	invite = forms.CharField(widget=forms.TextInput(attrs={'class':'grid_13'}))
	class Meta:
		model = Invite
		fields = ('to',)
