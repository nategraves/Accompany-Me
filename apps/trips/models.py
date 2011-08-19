from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

def pkgen():
	from base64 import b32encode
	from hashlib import sha1
	from random import random
	rude = ('fuck', 'shit', 'cunt', 'ass', 'hell', 'damn', 'fuk', 'bitch', 'bastard', 'kike',)
	bad_pk = True
	while bad_pk:
		pk = b32encode(sha1(str(random())).digest()).lower()[:6]
		bad_pk = False
		for rw in rude:
			if pk.find(rw) >= 0: bad_pk = True
	return pk

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
	mykey = models.CharField(max_length=6, primary_key=True, default=pkgen)

	def __unicode__(self):
		return "Trip to %s: %s" % (self.where, self.mykey)


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
