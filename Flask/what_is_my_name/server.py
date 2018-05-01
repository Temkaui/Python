from flask import Flask, redirect, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
	print request.form['first_name']
	return redirect ('/')

app.run(debug=True)