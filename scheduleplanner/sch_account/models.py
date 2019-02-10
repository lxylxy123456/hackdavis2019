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
	'ECS20': {'desc': 'Discrete Mathematics for Computer Science', 'preq': ['MAT21A']},
	'ECS36A': {'desc': 'Programming and Problem Solving', 'preq': []},
	'ECS36B': {'desc': 'Software Development and Object-Oriented Programming', 'preq': ['ECS36A']},
	'ECS50': {'desc': 'Computer Organization and Machine-Dependent Programming', 'preq': ['ECS36B']},
	'ECS36C': {'desc': 'Data Structures, Algorithms, and Programming', 'preq': ['ECS36B', 'ECS20']},
	'MAT21A': {'desc': 'Caculus', 'preq': []},
	'MAT21B': {'desc': 'Caculus', 'preq': ['MAT21A']},
	'MAT21C': {'desc': 'Caculus', 'preq': ['MAT21B']},
	'MAT22A': {'desc': 'Linear Algebra', 'preq': ['MAT21C']},
	'ECS132': {'desc': 'Probability and Statistical Modeling for Computer Science', 'preq': ['ECS36B', 'ECS50', 'MAT21C', 'MAT22A']},
	'ECS120': {'desc': 'Theory of Computation', 'preq': ['ECS20']},
	'ECS122A': {'desc': 'Algorithm Design and Analysis', 'preq': ['ECS20', 'ECS36C']},
#	'ECS122B': {'desc': 'Algorithm Design and Analysis', 'preq': ['ECS122A', 'ECS36C']},
	'ECS140A': {'desc': 'Programming Languages', 'preq': ['ECS50', 'ECS36C', 'ECS20']},
	'ECS150': {'desc': 'Operating Systems and System Programming', 'preq': ['ECS36C', 'ECS154A']},
	'ECS154A': {'desc': 'Computer Architecture', 'preq': ['ECS50']},
}

class UserClass(models.Model) :
	uid = models.IntegerField(u'User ID', null=False)
	cid = models.CharField(u'Class ID', max_length=10)
	rel = models.CharField(u'Relationship', max_length=10)
	def __str__(self):
		return "UserClass<%d, %s, %s>" % (uid, cid, rel)

