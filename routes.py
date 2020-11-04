# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created by CWENG at 2020-11-04
Current project: VeldiPython


"""
from flask import Flask
from flask import request



signal_interpreter_app = Flask(__name__)



@signal_interpreter_app.route("/")
def hello():
    return "Hello world!"

@signal_interpreter_app.route("/", methods=["POST"])
def mirror_data():
    data = request.get_json()
    print(data)
    return data

