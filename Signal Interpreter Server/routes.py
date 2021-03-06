# routes.py
from flask import Flask, request

signal_interpreter_app = Flask(__name__)


@signal_interpreter_app.route("/")
def start():
    return "Hello world!"


@signal_interpreter_app.route("/", methods=["POST"])
def mirror_data():
    data = request.get_json()
    print(data)
    return data





