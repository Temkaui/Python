from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt



def current_user(request):
	return User.objects.get(id = request.session['user_id'])

def index(request):
	return render(request, 'blog/index.html')

def register(request):
	check = User.objects.validateUser(request.POST)
	if request.method != 'POST':
		return redirect('/')
	if check[0] == False:
		for error in check[1]:
			messages.add_message(request, messages.INFO, error, extra_tags="registration")
			return redirect('/')
	if check[0] == True:
	
		user = User.objects.create(
			name = request.POST.get('name'),
			alias = request.POST.get('alias'),
			email = request.POST.get('email'),	
			password = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt()),
			birthdate = request.POST.get('birthday')
		)

		request.session['user_id'] = user.id
		return redirect('/dashboard')

def login(request):
	if request.method != 'POST':
		return redirect('/')
	user = User.objects.filter(email = request.POST.get('email')).first()

	if user and bcrypt.checkpw(request.POST.get('password').encode(), user.password.encode()):
		request.session['user_id'] = user.id
		return redirect('/quotes')
	else: 
		messages.add_message(request, messages.INFO, 'invalid credentials', extra_tags="login")
		return redirect('/')
	return redirect('/dashboard')

def logout(request):
		request.session.clear()
		return redirect('/')

def dashboard(request):
	user = current_user(request)

	context = {
		'user': user,
		'quotable_quotes': Quote.objects.exclude(favorites = user),
		'favorites': user.favorites.all()
	}

	return render(request, 'blog/dashboard.html', context)


def add_post(request):
	if request.method != 'POST':
		return redirect('/')
	
	check = Quote.objects.validateQuote(request.POST)
	if request.method != 'POST':
		return redirect('/dashboard')
	if check[0] == False:
		for error in check[1]:
			messages.add_message(request, messages.INFO, error, extra_tags="add_item")
			return redirect('/dashboard')
	if check[0] == True:

		quote = Quote.objects.create(
			content = request.POST.get('content'),
			poster = current_user(request),
			author = request.POST.get('author')
			)

		return redirect('/dashboard')
	return redirect('/dashboard')

def add_wall(request, id):

	user = current_user(request)
	favorite = Quote.objects.get(id=id)

	user.favorites.add(favorite)

	return redirect('/dashboard')

def remove_wall(request, id):

	user = current_user(request)
	favorite = Quote.objects.get(id=id)

	user.favorites.remove(favorite)

	return redirect('/dashboard')

def profile(request, id):

	user =  User.objects.get(id = id)
	context = {
		'user': user,
		'favorites': user.favorites.all()		
	}
	return render(request, 'blog/user.html', context)