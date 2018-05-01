from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def NinjaHome():
	return render_template("index.html")
@app.route("/ninja")
def NinjasHome():
	return render_template("ninja.html")

@app.route('/ninja/<color>')
def selection(color):
	return render_template('select.html', color = color)
app.run (debug = True)