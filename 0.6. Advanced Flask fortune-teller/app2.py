from flask import Flask, render_template,request,redirect,url_for
import random


app = Flask(__name__)

@app.route("/home", methods= ['GET', 'POST'])
def home():
	if request.method == 'GET':
	    
		return render_template("home.html")
	else:    
		birth = request.form['birthday']
		return redirect(url_for('furtune', birth=birth))

@app.route("/furtune/<birth>")
def furtune(birth):
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
	if len(birth)<10:
		response = my_fortunes[len(birth)]
		return render_template("furtune.html",furtune=response)
	else:
		num = random.randint(0,9)
		response = my_fortunes[num]
		return render_template("furtune.html", furtune = response)




if __name__ == '__main__':
    app.run(debug = True)