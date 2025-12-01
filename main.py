from flask import Flask, render_template, request, flash, redirect, url_for, Response


app: Flask = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    """
    Open home page
    :return: index html
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
