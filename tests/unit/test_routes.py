# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-server


"""
import pytest
from unittest.mock import patch, mock_open
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.routes import signal_interpreter_app


@pytest.mark.parametrize("sig", [
    "11",
    "27",
])
@patch.object(JsonParser, 'get_signal_title_from_id', return_value="dummy")
def test_interpret_signal(mock_get_signal_title_from_id, sig):
    '''
    Rename the function mirror_data() in routes.py to interpret_signal() instead.
    The function should receive the payload in the following format {"signal": "ID"} where ID is of type string.
    Then it should call the function that translates ID to a signal title so it can return the title in JSON-format to the client.
    :return:
    '''
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()
    payload = {"signal": sig}

    with my_app_instance as client:
        rv = client.post("/", json=payload)  # simulates a POST-message
        json_data = rv.get_json()
        assert json_data == "dummy"
        mock_get_signal_title_from_id.assert_called_with(sig)

