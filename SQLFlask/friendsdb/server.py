from flask import Flask, request, redirect, render_template, session, flash
from sqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    mysql.query_db("SELECT * FROM friends")
    return render_template('index.html')
@app.route('/friends', methods=['POST'])
def create():
    # add a friend to the database!
    return redirect('/')
app.run(debug=True)