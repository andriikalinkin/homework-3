from flask import Flask, render_template

import project_db


project_db.init_db()
app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>This is a homework-3 front page</h1>"


@app.route("/names")
def names():
    data = project_db.get_distinct_names()
    return render_template("names.html", data=data)


# @app.route("/tracks")
# def tracks():
#     pass
#
#
# @app.route("/tracks-sec")
# def tracks_sec():
#     pass


if __name__ == "__main__":
    app.run()
