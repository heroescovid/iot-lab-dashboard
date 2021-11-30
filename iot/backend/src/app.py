from flask import Flask,render_template
import paho as mqtt
app = Flask(__name__)
@app.route("/")
def holamundo():
    return "¡Hola Mundo!"
app.run(host = "0.0.0.0",port = 5050,debug = True)