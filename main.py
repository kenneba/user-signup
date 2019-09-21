from flask import Flask, escape, request
import os
import jinja2

app = Flask(__name__)

@app.route('/')
def signup():
    return "Signup is successfull"