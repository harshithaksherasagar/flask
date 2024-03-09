from flask import Flask, redirect,url_for, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/test",methods=["POST","GET"])
def test():
    if request.method =="POST":
        user = request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("navbar.html",content="Testing")
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"
if __name__ == "__main__":
    app.run()

