#!usr/bin/env python

# hellow world application for our Docker Course

# we would be using the flask framework

from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():

    return "Hellow world ... This is a First Docker app ... And a good beginning."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")