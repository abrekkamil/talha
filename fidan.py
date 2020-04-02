from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/Abrek/Desktop/Flask Tutorial/fidan/products.db"
db = SQLAlchemy(app)


@app.route("/")
def index():
    products = Products.query.all()
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/products")
def products():
    products = Products.query.all()
    return render_template("products.html", products=products)


@app.route("/add",methods=["POST"])
def addProduct():
    title = request.form.get("title")
    price = request.form.get("price")
    content = request.form.get("content")
    newProduct = Products(title=title, price=price, content=content)
    db.session.add(newProduct)
    db.session.commit()
    return redirect(url_for("products"))


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.String(200))
    price = db.Column(db.Float)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
