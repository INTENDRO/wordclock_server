from flask import Flask


app = Flask(__name__)
app.config["SECRET_KEY"] = '1432e842925bc56be708648cce938075'


from wordclockserver import routes