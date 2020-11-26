from unittest.mock import patch
from flask import Flask
import sys

from signal_interpreter_server.main import main
from signal_interpreter_server.routes import signal_interpreter_app, jp

@patch.object(Flask, "run")
def test_main(jp_instance):
    """
    * Use argparse to make it possible to run main.py with the argument --file_path where you can specify the path to
    the signal database file
    * Call load_file() during the startup of the server, i.e. when executing main.py
    :param mock_load_file:
    :param mock_run:
    :return:
    """
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    with my_app_instance as client:
        with patch.object(sys, "argv", ["main.main", "--file_path", "fixtures/test_basic.json"]):
            main()
            for d in jp.json_data['services']:
                rv = client.post("/", json={"signal": d["id"]})  # simulates a POST-message
                assert rv.get_json() == d["title"]