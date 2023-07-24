from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config={
  'apiKey': "AIzaSyCVl3WQQcDlR2UpitvR89upAH-wZ4Hd_ZI",
  'authDomain': "authentication-thing-4b7e7.firebaseapp.com",
  'projectId': "authentication-thing-4b7e7",
  'storageBucket': "authentication-thing-4b7e7.appspot.com",
  'messagingSenderId': "327586758924",
  'appId': "1:327586758924:web:8ebb211e92a3446a940929",
  'measurementId': "G-3878QWDK8H", "databaseURL": ""
  }
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
           return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
   return render_template("signup.html")


@app.route('/signin', methods=['GET', 'POST'])
def signin():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = 
auth.sign_in_with_email_and_password(email, password)
           return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
   return render_template("signin.html")


if __name__ == '__main__':
    app.run(debug=True)