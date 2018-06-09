from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
#from sqlalchemy import update
from sqlalchemy.sql import select

engine = create_engine('sqlite:///tutorial.db', echo = True)
 
app = Flask(__name__)
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = str(request.form['password'])
 
    Session = sessionmaker(bind = engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()
	
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
	
@app.route('/add', methods=['POST'])
def addItem():
    POST_NAME = str(request.form['name'])
    POST_YEAR = str(request.form['year'])
    Session = sessionmaker(bind = engine)
    s = Session()
    query = s.query(Car).update(Car.name.in_([POST_NAME]), Car.name.in_([POST_YEAR]))
    return render_template('addItem.html')

@app.route("/cars", methods=['GET'])
def getCars():
    Session = sessionmaker(bind = engine)
    s = Session()
    query = s.query(User).select()
    result = query
    return result

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug = True, host = '0.0.0.0', port = 4000)