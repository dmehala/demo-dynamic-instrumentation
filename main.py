from flask import Flask

app = Flask(__name__)


def g():
    return "<p>Hello, World!</p>"


def f():
    return g()


@app.route("/")
def hello_world():
    return f()
