from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

class UserAccount(models.Model):
	basic = models.OneToOneField(User, unique=True)
	major = models.CharField(u'Major', max_length=100, default='')
	year = models.IntegerField(u'Year', default=1)
	time_update = models.DateTimeField(u't_update', auto_now=True)
	time_create = models.DateTimeField(u't_create', auto_now_add=True)
	def __str__(self):
		return self.basic.email

ClassInfo = {
	
}

class UserClass(models.Model) :
	uid = models.IntegerField(u'User ID', null=False)
	cid = models.CharField(u'Class ID', max_length=10)
	rel = models.CharField(u'Relationship', max_length=10)
	def __str__(self):
		return "UserClass<%d, %s, %s>" % (uid, cid, rel)

