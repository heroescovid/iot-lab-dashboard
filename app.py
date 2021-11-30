from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def holamundo():
    return "¡Hola Mundo!"
app.run(host = "0.0.0.0",port = 5050,debug = True)