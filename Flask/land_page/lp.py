from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def Home():
	return render_template('index.html')

@app.route('/Ninjas')
def Ninjas():
	return render_template('Ninjas.html')

@app.route('/Dojo/new')
def Dojo():
	return render_template('Dojo.html')

app.run (debug=True)