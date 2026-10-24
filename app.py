

from flask import Flask, render_template, request, session
from flask_session import Session

#copy paste for stuff to work
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/",methods=["GET","POST"])
def intro():
    session.clear()
    if request.method == "POST":
                if session.get("mode", "light") == "light":
                    session["mode"] = "dark" 
                else:
                    session["mode"]="light"
    else:
        session.setdefault("mode", "light")
    return render_template("introduction.html", mode=session["mode"],current="/")

@app.route("/Interests",methods=["GET","POST"])
def interests():
    if request.method == "POST":
                if session.get("mode", "light") == "light":
                    session["mode"] = "dark" 
                else:
                    session["mode"]="light"
    else:
             session.setdefault("mode", "light")
    return render_template("interests.html", mode=session["mode"],current="/Interests")

@app.route("/Skills",methods=["GET","POST"])
def skills():
    if request.method == "POST":
            if session.get("mode", "light") == "light":
                session["mode"] = "dark" 
            else:
                session["mode"]="light"
    else:
         session.setdefault("mode", "light")
    return render_template("skills.html", mode=session["mode"],current="/Skills")

#no clue what this does but breaks if i don't use it
if __name__ == "__main__":
    app.run(debug=True)