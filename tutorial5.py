from flask import Flask, redirect,url_for, render_template, request,session,flash
from datetime import timedelta
app = Flask(__name__)
app.secret_key = "your_secret_key"
app.permanent_session_lifetime=timedelta(days=5)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/test",methods=["POST","GET"])
def test():
    if request.method =="POST":
        session.permanent=True
        user = request.form["nm"]
        session["custom_user_key"]= user
        return redirect(url_for("user"))
    else:
        if "custom_user_key" in session:
            return redirect(url_for("user"))
        return render_template("navbar.html")
@app.route("/user")
def user():
    if "custom_user_key" in session:
        user = session["custom_user_key"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("test"))
@app.route("/logout")
def logout():
    session.pop("custom_user_key",None)
    flash("you are logged out","info")
    return redirect(url_for("test"))
    
if __name__ == "__main__":
    app.run()
