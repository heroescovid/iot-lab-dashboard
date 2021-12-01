from flask import Flask,render_template
import paho as mqtt
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/sensores")
def grafica():
    return render_template("grafica.html")
app.run(host = "0.0.0.0",port = 5050,debug = True)