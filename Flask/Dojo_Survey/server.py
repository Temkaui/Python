from flask	import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def Home():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
	name = request.form['name']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	# return render_template('result.html')
	return render_template("result.html", rname=name, rlocation=location, rlanguage = language, rcomment = comment)


app.run(debug=True)
	