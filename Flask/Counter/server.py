from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = "crazy ninja"

@app.route("/")
def index():
	if 'count' not in session:
		session['count'] = 0
	session['count'] += 1
	return render_template('index.html', x = session['count'])

@app.route("/process", methods=["POST"])
def process():
	if int(request.form['action']) == 0:
		session['count'] = 0
	else:
		session['count'] += 1
	return redirect("/")

app.run(debug= True)