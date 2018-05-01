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
		'user' : user,
		'items': Item.objects.exclude(wishers__wisher_id = request.session['user_id']),
		'wishes': Wish.objects.filter(wisher_id=request.session['user_id']),
		'all': Wish.objects.all()
	}
	print data
	return render(request, 'main/dashboard.html', data)

def create(request):
	return render(request, 'main/create.html')

def process(request):
	response = Item.objects.Add_item(request.POST)
	if response["isValid"]:
		item = Item.objects.create(
			title = request.POST.get('item_name'),
			user = User.objects.get(id = request.session['user_id'])
			)
		return redirect("/create")
	else:
		for error in response["errors"]:
			messages.add_message(request, messages.ERROR, error)
		return redirect("/create")
def add_wish(request, wish_id):
	Wish.objects.create(wish_id=wish_id, wisher_id=request.session['user_id'])
	user = User.objects.get(id = request.session['user_id'])
	user.favorites.add(favorite)
	return redirect("/dashboard")

def remove_wish(request, wish_id):
	Wish.objects.get(wish_id=wish_id, wisher_id=request.session['user_id']).delete()
	return redirect("/dashboard")
