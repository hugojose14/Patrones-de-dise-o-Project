from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from passlib.hash import sha256_crypt
app = Flask(__name__)

#Ruta principal
@app.route("/")
def index():
    return render_template('index.html')

#Guia para utilizar la aplicación
@app.route("/about",methods=["PUT"])
def about():
    return render_template('about.html')

@app.route("/contact",methods=["PUT","POST"])
def contact():
    return render_template('contact.html')

@app.route("/sala",methods = ["PUT","POST"])
def sala():
    return render_template('sala.html')

@app.route("/login",methods=["GET","PUT"])  
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(port=3000,debug=True)