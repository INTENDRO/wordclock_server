from flask import render_template
from wordclockserver import app
from wordclockserver.forms import ColorPickerForm



@app.route("/", methods=["GET","POST"])
@app.route("/home", methods=["GET","POST"])
def home():
	form = ColorPickerForm()

	if form.validate_on_submit():
		if form.red_btn.data:
			print("RED!!")
		elif form.green_btn.data:
			print("GREEN!!")
		elif form.blue_btn.data:
			print("BLUE!!")
	return render_template("layout.html", form=form)

