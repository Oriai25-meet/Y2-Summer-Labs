from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/home")
def home():
	return render_template("home.html")

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
	furtunes=random.choice(my_fortunes)
	return render_template("furtune.html",furtune = furtunes)




if __name__ == '__main__':
    app.run(debug = True)