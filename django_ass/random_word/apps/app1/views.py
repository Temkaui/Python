from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
	if not 'attempt' in request.session:
		request.session['attempt'] = 0
	
	return render(request, "app1/index.html")

def generate(request):
	if not 'attempt' in request.session:
		request.session['attempt'] = 0
	request.session['attempt'] += 1
	request.session['word'] = get_random_string(length=14)
	request.session.modified = True

	return redirect("/")