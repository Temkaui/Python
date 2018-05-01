from flask import Flask, request, redirect, render_template, flash, session
import re, os, binascii, hashlib, sys, md5
from sqlconnection import MySQLConnector

def log(obj):
	print (obj, file==sys.stderr)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')
app.secret_key="crazy ninja"

@app.route('/')
def Home():
	return render_template('index.html')

@app.route('/login')
def login():
	username = request.form['username']

	data = mysql.query_db("SELECT username FROM users")
	for value in data:
		if value == username


@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/register/process', methods=['POST'])
def process():
	print "hello", request.form
	#validate first_name
	first_name = request.form['first_name']
	result = validator(first_name, "name")
	if not result["is_valid"]:
		flash("First name "+ result['response'], "registration_error")
		return redirect('/register')	
	
	#validate last name
	last_name = request.form['last_name']
	result = validator(last_name, "name")
	if not result["is_valid"]:
		flash("Last name "+ result['response'], "registration_error")
		return redirect('/register')
	
	#validate email
	email = request.form['email'].lower()
	# print "I am your email", email
	result = validator(email, "email")
	if not result["is_valid"]:
		flash(result['response'], "registration_error")
		return redirect('/register')

	#validate username	
	username = request.form['username']
	result = validator(username, "uname")
	if not result["is_valid"]:
		flash("username"+ result['response'], "registration_error")
		return redirect('/register')

	#validate password
	
	# while request.form['password'] == request.form['vpassword']:
	result = validator(request.form['password'], "password")
	if not result["is_valid"]:
		flash(result['response'], "registration_error")
		return redirect('/register')
	# flash(result['response'], "registration_error")
	# return redirect('/register')
	
	
	#generate salt and hash the password
	salt = str(binascii.b2a_hex(os.urandom(4)))
	hashed_password = hash_password(result, salt)
	
	#insert user data into database
	query = 'INSERT INTO login (first_name, last_name, email, username, password, salt) VALUES(:first_name, :last_name, :email, :username, :password, :salt)'
	data = {"first_name":first_name, "last_name":last_name, "email":email, "username": username, "password": hashed_password, "salt": salt}
	mysql.query_db(query, data)

	return redirect('/success')

@app.route('/success')
def success():
	return render_template('success.html')

def validator(input, type):
	# result = {"result":True, "response":""}
	log("input")
	log(input)
	if type == "email":
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$')
		temp = mysql.query_db("SELECT email FROM login")
		if input == temp[0]:
			return {"is_valid": False, "response":"this email is already registered."}
		if len(input) == 0:
			return {"is_valid":False, "response":"Email is required."}
		if not EMAIL_REGEX.match(input):
			return {"is_valid":False, "response":"Not a valid email."}
		#email is valid
		return {"is_valid":True, "response":""}

	if type == "name":
		if len(input) < 2:
			return {"is_valid":False, "response":" must be 2 or more characters"}
		if not input.isalpha():
			return {"is_valid":False, "response":" can not contain numbers or special characters"}
		#name is valid
		return {"is_valid":True, "response":""}
	
	if type == "uname":
		temp = mysql.query_db("SELECT username from login ")
		if input == temp[0]:
			return {"is_valid": False, "response":" this username is already taken"}
		if len(input) < 3:
			return {"is_valid":False, "response":" must be 2 or more characters"}
		if not input.isalnum():
			return {"is_valid":False, "response":" can not contain special characters"}
		#name is valid
		return {"is_valid":True, "response":""}
		
	if type == "password":
		if len(input)<8:
			return {"is_valid":False, "response":"Password must be at least 8 characters."}
		# if input != input[1]:
		# 	return {"is_valid":False, "response":"password does not match"}
		#password is valid
		return {"is_valid":True, "response":""}


def hash_password(password, salt):
	salted_password = str(password) + str(salt)
	return hashlib.md5(salted_password).hexdigest()


app.run(debug=True)