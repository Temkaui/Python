from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visitedcopy
def index(request):
	response = "Hello, I am your first request!"
	return HttpResponse(response)

def new(request):
	response = "this is a new blog"
	return HttpResponse(response)

def create(request):
	response = "Create blog in this page"
	return HttpResponse(response)

def number(request, number):
	response = "blog number is"
	return HttpResponse(response +" "+ number)

def edit(request, number):
	response = "edit blog number"
	return HttpResponse( response +" "+ number)
def delete(request, number):
	return HttpResponse("Delete blog number" + number)