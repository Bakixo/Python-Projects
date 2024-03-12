"""
from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL 
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt


app = Flask(__name__)

@app.route("/")
def ana_Sayfa():

    return render_template("index.html")
@app.route("/about")
def hakkimda():
    return render_template("about.html")
@app.route("/certificates")
def sertifikalar():
    return render_template("certificates.html")
@app.route("/communication")
def iletisim():
    return render_template("communication.html")
if __name__ == "__main__":
    app.run(debug=True)

    """