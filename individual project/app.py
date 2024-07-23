from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session 
import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyC8-M4PRPcttG2W06aywRKV3fiDRdXlXTw",
  'authDomain': "gallery-6067f.firebaseapp.com",
  'projectId': "gallery-6067f",
  'storageBucket': "gallery-6067f.appspot.com",
  'messagingSenderId': "1056672086759",
  'appId': "1:1056672086759:web:cf3e1f7cac0895d2910042",
  'measurementId': "G-Z8HDH5436F",
  "databaseURL":"https://gallery-6067f-default-rtdb.europe-west1.firebasedatabase.app/"}

app = Flask(__name__,template_folder="tamplates",static_folder = "static")
app.config['SECRET_KEY'] = 'super-secret-key'

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db =firebase.database()

@app.route("/", methods=["GET","POST"])
def signup():
	if request.method =="GET":
		return render_template("signup.html") 
	else:
		email = request.form['email']
		password = request.form['password']
		full_name = request.form['full_name']
		fav_img  = request.form['fav_img']
		login_session['user'] = auth.create_user_with_email_and_password(email, password)
		user_id = login_session['user']['localId']
		user = {'full_name':full_name, 'fav_img': fav_img}
		db.child("users").child(user_id).set(user)
		return redirect(url_for('home'))


@app.route("/signin",methods = ["GET","POST"])
def signin():
	if request.method=="POST":
		email = request.form['email']
		password = request.form['password']
		login_session['user'] = auth.sign_in_with_email_and_password(email, password)
		return redirect(url_for('home'))
	
	else:
		return render_template("signin.html")


@app.route("/home",methods=["GET","POST"])
def home():
	if request.method=="GET":
		return render_template("home.html") 
	else:
		user_id = login_session['user']['localId']
		gallery = {"img":request.form['img'],"category":request.form['category']}
		db.child("user_id").push(gallery)
		return redirect(url_for('thanks'))

@app.route("/thanks")
def thanks():
	return render_template("thanks.html") 


if __name__ == '__main__':
    app.run(debug=True)

