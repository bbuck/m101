import bottle
import pymongo
from bson.objectid import ObjectId
import hashlib

conn = pymongo.Connection("mongodb://localhost", safe=True)
db = conn.blog_test

users = db.users
sessions = db.sessions


# Hash and return a string
def hash_string(str_):
    md5 = hashlib.md5()
    md5.update(str_)
    return md5.hexdigest()


# Index Page
@bottle.get("/")
def index():
    return "This is a placeholder for the blog"


# Sign Up page
@bottle.get("/signup")
def sign_up():
    return bottle.template("login/signup")


# Create a new user
@bottle.post("/users")
def create_user():
    username = bottle.request.forms.username
    password = bottle.request.forms.password
    verify = bottle.request.forms.verify_password
    email = bottle.request.forms.email
    if not (username and password and verify):
        return bottle.redirect("/signup") 
    if password != verify:
        return bottle.redirect("/signup")
    if email.strip() == "":
        email = None
    password = hash_string(password)
    user = {"_id": username.strip(), "password": password, 
            "email": email.strip()}
    users.save(user)
    session = {"username": username}
    sessions.save(session)
    bottle.response.set_cookie("session", str(session["_id"]))
    return bottle.redirect("/welcome")


# Load the welcome page
@bottle.get("/welcome")
def welcome():
    session_id = ObjectId(bottle.request.get_cookie("session"))
    session = sessions.find_one({"_id": session_id}, 
                                {"username": 1, "_id": 0})
    return bottle.template("welcome", username=session["username"])


# Delete a session
@bottle.get("/logout")
def logout():
    session_id = bottle.request.get_cookie("session")
    sessions.remove({"_id": ObjectId(session_id)})
    bottle.response.delete_cookie("session")
    return bottle.redirect("/signup")


# Show the Login Screen
@bottle.get("/login")
def view_login():
    return bottle.template("login/login")


# Log a user in
@bottle.post("/login")
def login_user():
    username = bottle.request.forms.username
    password = hash_string(bottle.request.forms.password)
    user = users.find_one({"_id": username}, {"password": 1})
    if user is None or not (username and password):
        return bottle.redirect("/login")
    elif user["password"] != password:
        return bottle.redirect("/login")
    else:
        session = {"username": user["_id"]}
        sessions.save(session)
        bottle.response.set_cookie("session", str(session["_id"]))
        return bottle.redirect("/welcome")


bottle.run(host="localhost", port=3000)
