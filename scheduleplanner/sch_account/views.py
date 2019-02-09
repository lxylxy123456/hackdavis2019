import json

from django.http import HttpResponse

from django.shortcuts import render, render_to_response
from django.template.context_processors import csrf

class Snap :
	def record(request) :
		dict_render = {}
		dict_render.update(csrf(request))
		return dict_render
	def json(dict_render) :
		return HttpResponse(json.dumps(dict_render))
	def render(template, dict_render) :
		return render_to_response(template, dict_render)

def index(request):
	dict_render = Snap.record(request)
	dict_render['a'] = 'q'
	return Snap.render('a.html', dict_render)

def login(request) :
	dict_render = Snap.record(request)
	if request.method == 'POST' :
		dict_resp = {}
		if request.POST['username'] == request.POST['password'] :
			dict_resp['message'] = 'suc'
			dict_resp['redirect'] = '/'
		else :
			dict_resp['message'] = 'fail'
		return Snap.json(dict_resp)
	else :
		return Snap.render('login.html', dict_render)

