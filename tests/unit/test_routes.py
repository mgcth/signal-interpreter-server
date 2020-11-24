# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-server


"""
from unittest.mock import patch
from json_parser import JsonParser
from routes import signal_interpreter_app


@patch.object(JsonParser, 'get_signal_title_from_id', return_value="dummy")
def test_interpret_signal(mock_get_signal_title_from_ID):
    """
    Rename the function mirror_data() in routes.py to interpret_signal() instead.
    The function should receive the payload in the following format {"signal": "ID"} where ID is of type string.
    Then it should call the function that translates ID to a signal title so it can return the title in JSON-format to the client.
    :return:
    """
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    with my_app_instance as client:
        payload = {"signal": "11"}
        rv = client.post("/", json=payload)  # simulates a POST-message
        json_data = rv.get_json()
        assert json_data == "dummy"
        mock_get_signal_title_from_ID.assert_called_with("11")
