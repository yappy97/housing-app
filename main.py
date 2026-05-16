from flask import Flask, render_template, request, redirect

app = Flask(__name__)

listings = []

@app.route("/")
def home():
    return render_template("index.html", listings=listings)

@app.route("/add", methods=["POST"])
def add():
    listings.append({
        "location": request.form["location"],
        "price": request.form["price"],
        "type": request.form["type"]
    })
    return redirect("/")

if __name__ == "__main__":
    app.run()