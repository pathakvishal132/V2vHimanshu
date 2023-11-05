from flask import Flask, render_template
from pmain import app


@app.route("/")
def index():
    return render_template("home.html")
