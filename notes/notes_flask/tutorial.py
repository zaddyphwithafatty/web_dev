from flask import Flask, render_template, request, redirecnt, url_for

app = Flask(__name__)

@app.route("/", methods=["POST","GET"]) 
def home():
    if request.methdo == "POST":
        return redirect(url_for("user", name=request.form["name"]))
    return render_template("index.html")

@app.route("/contact")
def contact():
    return "<p>dont contact me. I don't want to tak to you.</p>"

@app.route("/<name>")
def user(name):
    return f"<h1> hello {name}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)