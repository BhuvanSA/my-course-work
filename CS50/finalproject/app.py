from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/achive.html")
def achive():
    return render_template("achive.html")


