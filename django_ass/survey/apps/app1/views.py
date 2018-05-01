from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
	return render(request, "app1/index.html")

def process(request):
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	return redirect('/result')

def result(request):
	return render(request, "app1/result.html")
