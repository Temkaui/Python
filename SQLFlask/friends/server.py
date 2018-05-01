from flask import Flask, render_template as render, request, redirect
# import the Connector function
from sqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'friendsdb')
# an example of running a query

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		# do post things
		query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
		mysql.query_db(query, request.form)
		return redirect("/")
	else:
		return render("index.html", friends=mysql.query_db("SELECT * FROM friends"))

app.run(debug=True)