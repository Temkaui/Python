# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages



def index(request):
	return render(request, 'main/index.html')

def register(request):
	response = User.objects.register(request.POST)
	if response["isValid"]:
		request.session["user_id"] = response["user"].id
		return redirect("/dashboard")
	else:
		for error in response["errors"]:
			messages.add_message(request, messages.ERROR, error)
		return redirect("/")

def login(request):
	response = User.objects.login(request.POST)
	if response["isValid"]:
		request.session["user_id"] = response["user"].id
		return redirect("/dashboard")
	else:
		for error in response["errors"]:
			messages.add_message(request, messages.ERROR, error)
		return redirect("/")

def logout(request):
	request.session.clear()
	return redirect("/")


def dashboard(request):
	user = User.objects.get(id = request.session['user_id'])
	data = {
		"user": user,
		"all_items": Items.objects.exclude(favorites = user),
		"wishes": user.wishes.all()
	}
	return render(request, 'main/dashboard.html', data)

def create(request):
	return render(request, 'main/create.html')

def process(request):
	response = Items.objects.Validate(request.POST)
	if response["isValid"]:
		all_items = Items.objects.create(
			item_name = request.POST.get('item_name'),
			poster = User.objects.get(id = request.session['user_id'])
			)
		return redirect("/dashboard")
	else:
		for error in response["errors"]:
			messages.add_message(request, messages.ERROR, error)
			return redirect("/dashboard")

def add_wish(request, id):

	user = User.objects.get(id = request.session['user_id'])
	wish = Items.objects.get(id=id)
	user.wishes.add(wish)

	return redirect('/dashboard')

def rem_wish(request, id):

	user = User.objects.get(id = request.session['user_id'])
	wish = Items.objects.get(id=id)
	user.wishes.remove(wish)

	return redirect('/dashboard')

def item(request, id):
	data = {
		'item' : Items.objects.get(id=id),
		'users' : Items.objects.get(id=id).favorites.all()	
		}
	return render(request, 'main/item.html', data)

def delete(request, id):
	b = Items.objects.get(id = id)
	b.delete()
	return redirect('/dashboard')

