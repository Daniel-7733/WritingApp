from flask import Flask, render_template, request
from time import strftime, localtime, struct_time

app: Flask = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    """
    Open home page

    :return: index HTML
    """

    return render_template("index.html")



@app.route("/start", methods=["GET", "POST"])
def start() -> str:
    """
    This function will get the words from textarea in HTML.

    :return: index HTML and words
    """
    text: str = request.form.get("note", "")
    return render_template("index.html", word=text)



@app.route("/start_btn", methods=["GET", "POST"])
def start_btn() -> str:
    """
    This function will save the initiate time

    :return: index HTML and current time
    """
    get_date: struct_time = localtime()
    current_time: str = strftime("%H:%M:%S", get_date)
    return render_template("index.html", now_time=current_time)


@app.post("/lose")
def lose() -> tuple[str, int]:
    """
    This one help will print "User Lost" if it takes more then 5 seconds to write.
    """
    print("User lost (5 seconds of no typing)")
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
