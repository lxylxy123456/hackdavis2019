# 
# Schedule Planner https://devpost.com/software/hackdavis2019-w5spun
# Copyright (C) 2018  lxylxy123456, Yiling Chen, jingyizhu, wyr
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# 

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
	'ECS120': {'desc': 'Theory of Computation', 'preq': ['ECS20']},
	'ECS122A': {'desc': 'Algorithm Design and Analysis', 'preq': ['ECS20', 'ECS36C']},
#	'ECS122B': {'desc': 'Algorithm Design and Analysis', 'preq': ['ECS122A', 'ECS36C']},
	'ECS132': {'desc': 'Probability and Statistical Modeling for Computer Science', 'preq': ['ECS36B', 'ECS50', 'MAT21C', 'MAT22A']},
	'ECS140A': {'desc': 'Programming Languages', 'preq': ['ECS50', 'ECS36C', 'ECS20']},
	'ECS150': {'desc': 'Operating Systems and System Programming', 'preq': ['ECS36C', 'ECS154A']},
	'ECS154A': {'desc': 'Computer Architecture', 'preq': ['ECS50']},
}

class UserClass(models.Model) :
	uid = models.IntegerField(u'User ID', null=False)
	cid = models.CharField(u'Class ID', max_length=10)
	rel = models.CharField(u'Relationship', max_length=10)
	def __str__(self):
		return "UserClass<%d, %s, %s>" % (self.uid, self.cid, self.rel)

