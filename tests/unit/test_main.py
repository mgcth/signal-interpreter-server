# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-server


"""
from unittest.mock import patch, mock_open
from flask import Flask
import sys
import logging

from signal_interpreter_server.main import main, init
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.routes import signal_interpreter_app


logger = logging.getLogger(__name__)


@patch("signal_interpreter_server.main.main")
@patch("signal_interpreter_server.main.__name__", "__main__")
def test_init(mock_main):
    """
    Test init function.
    :param mock_main:
    :return:
    """
    logger.debug("Start of %s function test log.", test_init.__name__)
    init()
    mock_main.assert_called_once()
    logger.debug("End of %s function test log.", test_init.__name__)


@patch.object(JsonParser, 'get_signal_title_from_id', return_value="dummy")
@patch.object(Flask, "run")
@patch.object(JsonParser, "load_file")
def test_main(mock_load_file, mock_run, mock_get_signal_title_from_id):
    """
    Test main function.
    :param mock_load_file:
    :param mock_run:
    :param mock_get_signal_title_from_id:
    :return:
    """
    logger.debug("End of %s function test log.", test_main.__name__)
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    with my_app_instance as client:
        with patch.object(sys, "argv", ["main.main", "--file_path", "data/signal_database.json"]):
            main()
            payload = {"signal": "11"}
            client.post("/", json=payload)  # simulates a POST-message
            mock_run.assert_called_once()
            mock_load_file.assert_called_with("data/signal_database.json")
    logger.debug("Start of %s function test log.", test_main.__name__)