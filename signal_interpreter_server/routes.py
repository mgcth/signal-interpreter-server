# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-server


"""
from flask import Flask, request, jsonify
from json_parser import JsonParser

jp = JsonParser()
signal_interpreter_app = Flask(__name__)


# @signal_interpreter_app.route("/")
# def start():
#     return "Hello world!"

@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """
    interpret signal
    :return:
    """
    data = request.get_json()
    print(jp.get_signal_title_from_id(data['signal']))
    return jsonify(jp.get_signal_title_from_id(data['signal']))
