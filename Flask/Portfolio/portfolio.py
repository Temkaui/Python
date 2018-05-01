from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Home():
	return render_template('index.html')

@app.route('/Projects')
def Projects():
	return render_template('Projects.html')

@app.route('/About')
def About():
	return render_template('About.html')

app.run (debug=True)