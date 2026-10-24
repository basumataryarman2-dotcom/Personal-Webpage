import os
import secrets

from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/",methods=["GET","POST"])
def intro():
    if request.method == "POST":
        session["mode"] = "dark" if session.get("mode", "light") == "light" else "light"
    else:
        session.setdefault("mode", "light")

    return render_template("introduction.html", mode=session["mode"])


if __name__ == "__main__":
    app.run(debug=True)