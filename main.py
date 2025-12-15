from flask import Flask, render_template, request, flash, redirect, url_for, Response
from time import strftime, localtime, struct_time

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
    """
    This function will get the words from textarea in html.

    :return: index html and words
    """
    text: str = request.form.get("note", "")
    return render_template("index.html", word=text)



@app.route("/start_btn", methods=["GET", "POST"])
def start_btn() -> str:
    """
    This function will save the initiate time

    :return: index html and current time
    """
    get_date: struct_time = localtime()
    current_time: str = strftime("%H:%M:%S", get_date)
    return render_template("index.html", now_time=current_time)


@app.post("/lose")
def lose():
    print("User lost (5 seconds of no typing)")
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
