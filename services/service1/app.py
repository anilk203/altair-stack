from flask import Flask, redirect, url_for, render_template
import datetime
import os
import csv
import json
import sys
import uuid

app = Flask(__name__)

@app.route("/service1/")
def home():
    return render_template("index.html", utc_dt=datetime.datetime.utcnow())

@app.route("/service1/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)    
    app.run_server(debug=True)