from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, my world!"

@app.route("/<name>")
def ret(name=None):
    if name:
        return f"Hello {name}!"
    else:
        return "Hello, world!"

@app.route("/admin")
def admin():
    return redirect(url_for('ret', name="from admin"))

@app.route("/rent")
def rent():
    return "Hello, my rent!"

if __name__ == "__main__":
    app.run()
