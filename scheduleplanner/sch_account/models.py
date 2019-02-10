from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

class UserAccount(models.Model):
	basic = models.OneToOneField(User, unique=True)
	major = models.CharField(u'major', max_length=100, default='')
	year = models.IntegerField(u'year', default=1)
	time_update = models.DateTimeField(u't_update', auto_now=True)
	time_create = models.DateTimeField(u't_create', auto_now_add=True)
	
	def __str__(self):
		return self.basic.email

