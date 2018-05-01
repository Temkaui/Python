# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from models import *

def index(request):
	date = strftime("%Y-%m-%d", gmtime())
	time = strftime("%H:%M:%S", gmtime())
	print get_random_string(length=14)
	context = {
		"date": date,
		"time": time
	}
	return render(request, "blogs/index.html", context)

def new(request):
	return render(request, "blogs/new.html")

def create(request):
	return redirect("/new")

def display(request, number):
	return HttpResponse("placeholder to display blog {}" .format(number))

def edit(request, number):
	return HttpResponse("placeholder to edit blog {}" .format(number))

def delete(request, number):
	return redirect ('/')
   