from flask import Flask, render_template,request,redirect,url_for
from flask import session as login_session
import random

app = Flask(__name__)

app.config['SECRET_KEY']="PASSWORD"






@app.route("/", methods= ['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template("login.html")
	else:    
		login_session['user_name'] = request.form['username']
		login_session['birthday'] = request.form['birthday']
		return redirect(url_for('home'))

@app.route("/home",methods= ['GET', 'POST'])
def home():
	user_name1 = login_session['user_name']
	birthday = login_session['birthday']
	return render_template("home.html",user_name = user_name1 ,birth_month=birthday)


@app.route("/furtune")
def furtune():
	my_fortunes = ["Your hard work will soon be rewarded in unexpected ways.",
	"A pleasant surprise is waiting for you around the corner.",
	"Trust your intuition; it will lead you to great things.",
	"Good things come to those who wait patiently.",
	"Your creativity will bring you joy and success.",
	"Be open to new opportunities; they will bring you prosperity.",
	"Your kindness will attract positive energy into your life.",
	"Embrace change; it will lead to growth and fulfillment.",
	"Take time to relax and recharge; it will benefit you greatly.",
	"Love and happiness are on their way to you soon."]
	if len(login_session['birthday'])<10:
		login_session['furtune'] = my_fortunes[len(login_session['birthday'])]
		return render_template("furtune.html",furtune=login_session['furtune'])
	else:
		num = random.randint(0,9)
		login_session['furtune'] = my_fortunes[num]
		return render_template("furtune.html", furtune = login_session['furtune'])




if __name__ == '__main__':
    app.run(debug = True)