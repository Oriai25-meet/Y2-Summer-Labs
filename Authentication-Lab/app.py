from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase


firebaseConfig = {
  "apiKey": "AIzaSyDzdC8BxZ8vggsAGF_jIlQVrjElaMm3xrk",
  "authDomain": "loginin-db2f2.firebaseapp.com",
  "projectId": "loginin-db2f2",
  "storageBucket": "loginin-db2f2.appspot.com",
  "messagingSenderId": "120873802287",
  "appId": "1:120873802287:web:86ecd21ee10fe0fda404da",
  "measurementId": "G-RG0VBHS94Q",
  "databaseURL": ""}

app = Flask(__name__,template_folder="templates",static_folder = "static")
app.config['SECRET_KEY'] = 'super-secret-key'

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()



@app.route("/", methods=["GET","POST"])
def signup():
	if request.method =="GET":
		return render_template("signup.html") 
	else:
		try:
			email = request.form['email']
			password = request.form['password']
			login_session['user'] = auth.create_user_with_email_and_password(email, password)
			login_session["quotes"] = []
			return redirect(url_for('home'))
		except:
			error = "something went wrong, email in used"
			login_session['error']= error
			return redirect(url_for('error'))

@app.route("/error")
def error():
	error_massege = login_session['error']
	return render_template('error.html',error_massege = error_massege)




@app.route("/signin",methods=["GET","POST"])
def signin():
	if request.method=="POST":
		try:
			email = request.form['email']
			password = request.form['password']
			login_session['user'] = auth.sign_in_with_email_and_password(email, password)
			if "quotes" not in login_session:
				login_session["quotes"] = []
			return redirect(url_for('home'))
		except:
			error = "something went wrong, password incorrect"
			login_session['error']= error
			return redirect(url_for('error'))
	else:
		return render_template("signin.html") 

@app.route("/home",methods=["GET","POST"])
def home():
	if request.method=="GET":
		return render_template("home.html") 
	else:
		message = request.form['message']
		login_session['quotes'].append(message)
		login_session.modified = True
		return redirect(url_for('thanks'))

@app.route("/signout", methods=["POST","GET"])
def signout():
	if request.method == "POST":
		return redirect(url_for('signin'))


@app.route("/thanks")
def thanks():
	return render_template("thanks.html") 

@app.route("/display")
def display():
	list_message = login_session['quotes']
	return render_template("display.html",list_message=list_message) 

if __name__ == '__main__':
    app.run(debug=True)
