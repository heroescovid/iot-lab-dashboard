from flask import Flask,render_template,url_for
import paho as mqtt
app = Flask(__name__)
@app.route("/")
def holamundo():
    return render_template("index.html")
app.run(host = "0.0.0.0",port = 5050,debug = True)