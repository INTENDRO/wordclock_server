from flask_wtf import FlaskForm
from wtforms import SubmitField

class ColorPickerForm(FlaskForm):
	red_btn = SubmitField("Red")
	green_btn = SubmitField("Green")
	blue_btn = SubmitField("Blue")
