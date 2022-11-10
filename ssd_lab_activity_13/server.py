from flask import Flask, render_template, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import json
from flask_login import (LoginManager, login_manager, login_user, logout_user, login_required, UserMixin)

app = Flask(__name__)
# conn = sqlite3.connect('user.db', check_same_thread=False)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = "yash"
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    # x = 11
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50), unique=True)

class movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.Integer, db.ForeignKey('user.id'))


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/user/signup", methods=['POST'])
def signup():
    res = request.get_json()
    name = res["name"]
    email =  res["email"]
    password =res["password"]

    newUser = User(name=name, email=email, password=password)
    db.session.add(newUser)
    db.session.commit()
    # print(name)
    response = {"message":"user created successfully"} 
    return jsonify(response)

@app.route("/user/signin", methods=['POST'])
def signin():
    response = {"message":"user created successfully"} 
    res = request.get_json()
    email =  res["email"]
    password =res["password"]
    requestUser = User.query.filter_by(email=email).first()
    if requestUser is not None:
        if(requestUser.password == password):
            login_user(requestUser)
            response["message"] = "loggedin successfully"
        else:
            response["message"] = "Incorrect password"
    else:
        response["message"] = "Invalid email"


    # print(name)
    return jsonify(response), 200

@app.route("/user/signout", methods=['POST'])
def signout():
    logout_user()
    response = {"message":"log out successfully"} 

    # print(name)
    return jsonify(response), 200

@app.route("/seats/available", methods=['GET'])
@login_required
def giveInfo():
    Response ={
                    "seats": [
                    {
                    "seat": "A1",
                    "price": 100
                    },
                    {
                    "seat": "A2",
                    "price": 100
                    }
                    ],
                    "seatsAvailable": 100,
                }
    return jsonify(Response)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)