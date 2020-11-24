# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-server


"""
from unittest.mock import patch, mock_open
from flask import Flask
import sys

from signal_interpreter_server.main import main, init
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.routes import signal_interpreter_app


@patch("signal_interpreter_server.main.main")
@patch("signal_interpreter_server.main.__name__", "__main__")
def test_init(mock_main):
    init()
    mock_main.assert_called_once()


@patch.object(JsonParser, 'get_signal_title_from_id', return_value="dummy")
@patch.object(Flask, "run")
@patch.object(JsonParser, "load_file")
def test_main(mock_load_file, mock_run, mock_get_signal_title_from_id):
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
        with patch.object(sys, "argv", ["main.main", "--file_path", "data/signal_database.json"]):
            main()
            payload = {"signal": "11"}
            client.post("/", json=payload)  # simulates a POST-message
            mock_run.assert_called_once()
            mock_load_file.assert_called_with("data/signal_database.json")



