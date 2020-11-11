from flask import Flask
from flask import request
from json_parser import parsejson

signal_interpreter_app = Flask(__name__)

@signal_interpreter_app.route("/")
def start():
    return "Hello, World!"

@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    data = request.get_json()
    title = parsejson.get_signal_title(data["signal"])
    return title