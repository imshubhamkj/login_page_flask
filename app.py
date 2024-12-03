from flask import Flask # type: ignore
from markupsafe import escape


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>hello world shubham</p>"

@app.route("/user/<username>")
def hello(username):
    return f"<p>hello world {escape(username)}</p>"

@app.route("/users/<int:id>")
def hi(id):
    return f"<p>hello world {escape(id)}</p>"