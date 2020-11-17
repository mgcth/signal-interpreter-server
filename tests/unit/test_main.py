# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-server


"""

from unittest.mock import patch, mock_open
from flask import Flask
import sys

from main import main
from json_parser import JsonParser
from routes import signal_interpreter_app



@patch.object(JsonParser, 'get_signal_title_from_ID', return_value="dummy")
@patch.object(Flask, "run")
@patch.object(JsonParser, "load_file")
def test_main(mock_load_file, mock_run, mock_get_signal_title_from_ID):
    '''
    * Use argparse to make it possible to run main.py with the argument --file_path where you can specify the path to the signal database file
    * Call load_file() during the startup of the server, i.e. when executing main.py
    :param mock_load_file:
    :param mock_run:
    :return:
    '''
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    with my_app_instance as client:
        with patch.object(sys, "argv", ["main.main", "--file_path", "./signal_database.json"]):
            main()
            payload = {"signal": "11"}
            client.post("/", json=payload)  # simulates a POST-message
            mock_run.assert_called_once()
            mock_load_file.assert_called_with("./signal_database.json")



