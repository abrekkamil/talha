from flask import Flask, render_template, redirect, url_for, request


app = Flask(__name__)
app.secret_key = "abrekblog"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)