from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class BaseModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	deleted = models.BooleanField(default=False)

	class Meta:
		abstract = True

class Trip(BaseModel):
	#For now I'll just save when as text
	when = models.CharField(max_length=255, blank=True, null=True)
	where = models.CharField(max_length=255, blank=True, null=True)
	author = models.ForeignKey(User, blank=True, null=True)
	private = models.BooleanField(default=False)

	def __unicode__(self):
		return "Trip # %s to %s" % (self.id, self.where)

class TripAdmin(BaseModel):
	trip = models.ForeignKey(Trip)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return "%s admin" % self.user.username

class Why(BaseModel):
	why = models.TextField()
	trip = models.ForeignKey(Trip)

	def __unicode__(self):
		return "#%s Why: %s" % (self.trip.id, self.why)

class Who(BaseModel):
	# Who will just be Facebook to start off
	who = models.CharField(max_length=255)
	trip = models.ForeignKey(Trip)

	def __unicode__(self):
		return "#%s with %s" % (self.trip.id,self.who)

admin.site.register(Trip)
admin.site.register(Why)
admin.site.register(Who)
admin.site.register(TripAdmin)
