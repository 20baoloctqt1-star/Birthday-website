from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/password")
def password():
    return render_template("password.html")


@app.route("/check", methods=["POST"])
def check():

    password = request.form["password"]

    if password == "maiandethuong":
        return render_template("surprise.html")

    return "Wrong password"


if __name__ == "__main__":
    app.run(debug=True)
