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

import json

from django.http import HttpResponse
from django.http import HttpResponseRedirect as Http302
from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf
from django.utils.safestring import mark_safe

from django.contrib import auth

from .models import *

class Snap :
	def record(request) :
		dict_render = { 'request': request }
		dict_render.update(csrf(request))
		return dict_render
	def success(dict_render) :
		dict_render['stat'] = 'success'
		return Snap.json(dict_render)
	def error(dict_render) :
		dict_render['stat'] = 'warning'
		return Snap.json(dict_render)
	def json(dict_render) :
		return HttpResponse(json.dumps(dict_render))
	def render(template, dict_render) :
		return render_to_response(template, dict_render)
	def redirect(location) :
		return Http302(location)

def home(request):
	if not request.user.is_authenticated() :
		return Snap.redirect('/login/')
	if request.method == 'POST' :
		data = {}
		for y in range(4) :
			for q in range(3) :
				for l in range(5) :
					cname = request.POST['%s_%s_%s' % (y, q, l)]
					if cname :
						if cname in data :
							return Snap.error({'msg': 'You are taking %s multip'
														'le times' % cname})
						data[cname] = y, q, l
		UserClass.objects.filter(uid=request.user.id).update(rel="")
		for i in data :
			qry = UserClass.objects.filter(uid=request.user.id, cid=i)
			if qry.exists() :
				qry.update(rel='%s_%s_%s' % data[i])
			else :
				UserClass(uid=request.user.id, cid=i, rel='%s_%s_%s' % data[i]).save()
		return Snap.success({'msg': 'class saved successfully', 'reload': 't'})
	else :
		dict_render = Snap.record(request)
		print(list(ClassInfo))
		dict_render['user'] = request.user
		dict_render['useraccount'] = UserAccount.objects.get(basic_id=request.user.id)
		dict_render['year'] = {
			1: 'Freshman', 
			2: 'Sophomore', 
			3: 'Junior', 
			4: 'Senior', 
			5: 'Super Senior', 
			6: 'Super Senior', 
		}.get(UserAccount.objects.get(basic_id=request.user.id).year, str(UserAccount.objects.get(basic_id=request.user.id).year))
		dict_render['class_list'] = list(map(lambda x: (x, x[:3] + ' ' + x[3:]), ClassInfo))
		dict_render['classes'] = ClassInfo
		dict_render['Y4'] = list(zip(range(4), ['First', 'Second', 'Third', 'Forth']))
		dict_render['Q3'] = list(zip(range(3), ['Fall', 'Winter', 'Spring']))
		dict_render['L5'] = range(5)
		dict_render['json_class_list'] = mark_safe(json.dumps(list(ClassInfo)))
		dict_render['json_classes'] = mark_safe(json.dumps(ClassInfo))
		userclass = []
		for uc in UserClass.objects.filter(uid=request.user.id) :
			if uc.rel :
				userclass.append([uc.cid, uc.rel])
		dict_render['userclass'] = mark_safe(json.dumps(userclass))
		return Snap.render('home1.html', dict_render)

def login(request) :
	dict_render = Snap.record(request)
	if request.user.is_authenticated() :
		return Snap.redirect('/')
	if request.method == 'POST' :
		dict_resp = {}
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is None or not user.is_active:
			return Snap.error({'msg': 'Incorrect username or password'})
		auth.login(request, user)
		dict_resp['msg'] = 'Login successful'
		dict_resp['redirect'] = '/'
		return Snap.success(dict_resp)
	else :
		return Snap.render('login.html', dict_render)

def logout(request) :
	auth.logout(request)
	return Snap.redirect('/')

def register(request) :
	dict_render = Snap.record(request)
	if request.user.is_authenticated() :
		return Snap.redirect('/')
	if request.method == 'POST' :
		username = request.POST['username']
		password = request.POST['password']
		if not username or not password :
			return Snap.error({'msg':'Please complete form before submitting.'})
		if password != request.POST['password2'] :
			return Snap.error({'msg': 'Passwords do not match.'})
		if User.objects.filter(username=username).exists() :
			return Snap.error({'msg': 'Username already used.'})
		try :
			year = int(request.POST['year'])
			if year not in range(1, 7) :
				raise ValueError
		except ValueError :
			return Snap.error({'msg': 'Invalid year.'})
		u = User(username=username)
		u.set_password(password)
		u.save()
		ua = UserAccount(basic=u, major='0/0', year=year)
		ua.save()
		user = auth.authenticate(username=username, password=password)
		auth.login(request, user)
		dict_resp = {}
		dict_resp['msg'] = 'Register successful'
		dict_resp['redirect'] = '/'
		return Snap.success(dict_resp)
	else :
		return Snap.render('register.html', dict_render)

