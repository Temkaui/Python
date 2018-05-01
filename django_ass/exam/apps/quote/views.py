# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages



def index(request):
	return render(request, 'quote/index.html')

def register(request):
	response = User.objects.register(request.POST)
	if response["isValid"]:
		request.session["user_id"] = response["user"].id
		return redirect("/quotes")
	else:
		for error in response["errors"]:
			messages.add_message(request, messages.ERROR, error)
		return redirect("/")

def login(request):
	response = User.objects.login(request.POST)
	if response["isValid"]:
		request.session["user_id"] = response["user"].id
		return redirect("/quotes")
	else:
		for error in response["errors"]:
			messages.add_message(request, messages.ERROR, error)
		return redirect("/")

def logout(request):
	request.session.clear()
	return redirect("/")


def quotes(request):
	user = User.objects.get(id = request.session['user_id'])
	data = {
		"user": user,
		"all_items": Items.objects.exclude(favorites = user),
		"favorites": user.wishes.all()
	}
	return render(request, 'quote/quotes.html', data)

def process(request):
	response = Quote.objects.validateQuote(request.POST)
	if response["isValid"]:
		quote = Quote.objects.create(
			content = request.POST.get('content'),
			poster = User.objects.get(id = request.session['user_id']),
			author = request.POST.get('author')
			)
		return redirect("/quotes")
	else:
		for error in response["errors"]:
			messages.add_message(request, messages.ERROR, error)
			return redirect("/quotes")

def add_to_list(request, id):

	user = User.objects.get(id = request.session['user_id'])
	favorite = Quote.objects.get(id=id)
	user.favorites.add(favorite)

	return redirect('/quotes')

def rem_from_list(request, id):

	user = User.objects.get(id = request.session['user_id'])
	favorite = Quote.objects.get(id=id)
	user.favorites.remove(favorite)

	return redirect('/quotes')

def profile(request):
	user = User.objects.get(id = request.session['user_id'])
	data = {
		"user": user,
		"favorites": user.favorites.all()
	}
	return render(request, 'quote/profile.html', data)


