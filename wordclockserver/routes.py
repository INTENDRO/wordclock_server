from flask import render_template
from wordclockserver import app



@app.route("/")
@app.route("/home")
def home():
	return render_template("layout.html")

