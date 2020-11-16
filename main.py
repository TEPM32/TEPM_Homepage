from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("main_page.html")


@app.route("/about_me")
def about_me():
    return render_template("about_me.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/gallery")
def gallery():
    return render_template("gallery.html")


if __name__ == "__main__":
    app.run()
