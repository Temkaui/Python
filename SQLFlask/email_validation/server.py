from flask import Flask, render_template, request, redirect, flash
import re
from sqlconnection import MySQLConnector

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key="crazy ninja"

mysql = MySQLConnector(app, 'mydb')

@app.route("/")
def home():
	return render_template('index.html')

@app.route("/success/add", methods=["POST"])
def process():
	if len(request.form['email']) == 0:
		flash("Email field is empty")
		return redirect('/')
	if not EMAIL_REGEX.match(request.form['email']):
		flash("this is not an email")
		return redirect('/')
	
	mysql.query_db("INSERT INTO users(email, created_at) Values(:email, now())", {"email": request.form['email']})
	return redirect('/success')

@app.route('/success')
def success():
	data = mysql.query_db("SELECT id, email, DATE_FORMAT(created_at, '%m/%e/%y %l:%i %p') AS date FROM users")
	
	return render_template("success.html", data = data)

app.run(debug=True)
