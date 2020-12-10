"""
Integration test for main.
"""
# pylint: disable=missing-function-docstring
import sys
import os
from unittest.mock import patch
import pytest
from flask import Flask


from signal_interpreter_server.main import main
from signal_interpreter_server.routes import signal_interpreter_app


CURR_DIR = os.path.abspath(os.path.dirname(__file__))


@pytest.mark.parametrize("file, services_index, id_index", [
    (os.path.join(CURR_DIR, "fixtures", "test_basic.json"), "services", "id"),
    (os.path.join(CURR_DIR, "fixtures", "test_basic.xml"), "services/service", "@id"),
])
@patch.object(Flask, "run")
def test_main(generic_parser_instance, file, services_index, id_index):
    """
    * Use argparse to make it possible to run main.py with the argument --file_path where you can specify the path to
    the signal database file
    * Call load_file() during the startup of the server, i.e. when executing main.py
    :param generic_parser:
    :return:
    """
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    with my_app_instance as client:
        with patch.object(sys, "argv", ["main.main", "--file_path", file]):
            main()
            for data in generic_parser_instance.get_parser().data[services_index]:
                response_value = client.post("/", json={"signal": data[id_index]})   # simulates a POST-message
                assert response_value.get_json() == data["title"]
