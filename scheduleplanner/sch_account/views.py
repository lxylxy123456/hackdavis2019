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
	dict_render = Snap.record(request)
	dict_render['class_list'] = mark_safe(json.dumps(list(ClassInfo)))
	dict_render['classes'] = mark_safe(json.dumps(ClassInfo))
	return Snap.render('home.html', dict_render)

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
		u = User(username=username)
		u.set_password(password)
		u.save()
		ua = UserAccount(basic=u, major='0/0', year=0)
		ua.save()
		user = auth.authenticate(username=username, password=password)
		auth.login(request, user)
		dict_resp = {}
		dict_resp['msg'] = 'Register successful'
		dict_resp['redirect'] = '/'
		return Snap.success(dict_resp)
	else :
		return Snap.render('register.html', dict_render)

