from flask import Flask, render_template, request, flash, redirect, url_for, Response


app: Flask = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    """
    Open home page
    :return: index html
    """

    return render_template("index.html")


# TODO: Get the value from textarea in html
# TODO: I need to have timer for user. If user take more then 5 second to write then function will remove all the text
@app.route("/start", methods=["GET", "POST"])
def start() -> str:
    word: str = ""
    if request.method == "POST":
        while True:
            text: str = request.form.get("note")
            word += text

    return render_template("index.html", word=word)


if __name__ == "__main__":
    app.run(debug=True)
