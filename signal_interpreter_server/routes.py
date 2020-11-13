from flask import Flask, request, jsonify
from json_parser import JsonParser

jp = JsonParser()
signal_interpreter_app = Flask(__name__)

@signal_interpreter_app.route("/")
def start():
    return "Hello world!"

@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    data = request.get_json()
    return jsonify(jp.get_signal_title_from_ID(data['signal']))