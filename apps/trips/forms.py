from django import forms

from trips.models import Trip, Why, Who

class IndexForm(forms.Form):
	where = forms.CharField(widget=forms.TextInput(attrs={'class':'alpha grid_8 where'}))
	private = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox'}))
	when = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'alpha grid_8 where'}))
	why = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'alpha grid_8 where'}))
	who = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'alpha grid_8 where'}))

class AltIndexForm(forms.Form):
	where = forms.CharField(widget=forms.TextInput(attrs={'class':'alpha grid_8 where'}))
	private = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'checkbox'}))
	when = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'alpha grid_3 where'}))
	why = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'alpha grid_3 where'}))
	who = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'alpha grid_3 where'}))

class TripForm(forms.ModelForm):
	when = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'alpha grid_8 where'}))
	where = forms.CharField(widget=forms.TextInput(attrs={'class':'alpha grid_8 where'}))
	class Meta:
		model = Trip
		fields = ('when', 'where',)

class WhyForm(forms.ModelForm):
	why = forms.CharField(widget=forms.TextInput(attrs={'class':'alpha grid_8 where'}))
	class Meta:
		model = Why
		fields = ('why',)

class WhoForm(forms.ModelForm):
	who = forms.CharField(widget=forms.TextInput(attrs={'class':'alpha grid_8 where'}))
	class Meta:
		model = Who
		fields = ('who',)
