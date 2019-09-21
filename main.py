from flask import Flask, escape, request, redirect, render_template
import string
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    confirm_password_error = ''
    email_error = ''

    if (len(username)>= 3 and len(username) <= 20) and not (" " in username):
        username_error = ""
    else: 
        username_error ="Username does not meet requirements"

    if len(password)>= 3 and len(password) <= 20 and not (" " in password):
        password_error=""
    else:
        password_error="Password does not meet requirements"

    if password == confirm_password:
        confirm_password_error=""
    else:
        confirm_password_error = "Passwords do not match"

    if len(email)==0:
        email_error=""
    else:
        if (len(email)>= 3 and len(email) <= 20) and not (" " in email) and ("." in email) and ("@" in email):
            email_error=""
        else:
            confirm_password_error = "Please select a valid email address"

    if not username_error and not password_error and not confirm_password_error and not email_error:
        return render_template("submission.html", username=username)
    else: 
        return render_template("index.html", username_error=username_error, email_error=email_error, confirm_password_error=confirm_password_error, password_error=password_error, username=username,email=email, password=password, confirm_password=confirm_password)

app.run()