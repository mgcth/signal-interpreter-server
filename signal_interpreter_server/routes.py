# routes.py
"""
Contains routing methods.
"""
from flask import Flask, request, jsonify
from signal_interpreter_server.json_parser import JsonParser

signal_interpreter_app = Flask(__name__)
json_parser = JsonParser()


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():  # pylint: disable=missing-function-docstring
    data = request.get_json()
    interpretation = json_parser.get_interpretation(data["signal"])
    return jsonify(interpretation)
