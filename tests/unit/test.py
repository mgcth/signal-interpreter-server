import sys
import json
from flask import Flask, jsonify, request
from unittest.mock import patch, mock_open
from argparse import Namespace
from json_parser import ParseJSON
from routes import start, interpret_signal
from main import main, get_args

app = Flask(__name__)

def test_load_files_test():
    pj = ParseJSON()
    with patch("builtins.open", mock_open(read_data=json.dumps({"id": "1"}))):
        pj.load_file("data\\signal_database.json")
        assert pj.data == {"id": "1"}

def test_get_signal_title_test():
    ctx = app.app_context()
    ctx.push()

    pj = ParseJSON()
    data = {"services": [{"id": "1", "title": "a"}, {"id": "2", "title": "b"}]}
    with patch("builtins.open", mock_open(read_data=json.dumps(data))):
        pj.load_file("data\\signal_database.json")

    assert pj.get_signal_title("1").data == jsonify("a").data

def test_start_hello_world():
    assert start() == "Hello, World!"

@patch.object(ParseJSON, "get_signal_title")
def test_interpret_signal_test(mock_get_signal_title):
    with app.test_client() as c:
        rv = c.post("/endpoint", json = {"signal": "1"})
        json_data = rv.get_json()

        tmp = 1
        mock_get_signal_title.return_value = "1"#json_data["signal"]
        assert interpret_signal() == "1"

@patch.object(sys, "argv", ["signal-interpreter-server", "-f", "test_path"])
def test_get_args_test():
    assert get_args() == Namespace(file_path="test_path")

# # how?
# @patch.object(ParseJSON, "load_file")
# @patch(main.get_args)
# def test_main_test(mock_load_file, mock_get_args):
#