# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-server


"""
import pytest
from unittest.mock import patch, mock_open
import logging
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.routes import signal_interpreter_app
from signal_interpreter_server.exceptions import JsonParserGetTitleError


logger = logging.getLogger(__name__)


@pytest.mark.parametrize("sig", [
    "11",
    "27",
])
@patch.object(JsonParser, 'get_signal_title_from_id', return_value="dummy")
def test_interpret_signal(mock_get_signal_title_from_id, sig):
    """
    Testing interpret_signal.
    :param mock_get_signal_title_from_id:
    :param sig:
    :return:
    """
    logger.debug("Start of %s function test log.", test_interpret_signal.__name__)
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()
    payload = {"signal": sig}

    with my_app_instance as client:
        rv = client.post("/", json=payload) # simulates a POST-message
        json_data = rv.get_json()
        assert json_data == "dummy"
        mock_get_signal_title_from_id.assert_called_with(sig)
    logger.debug("End of %s function test log.", test_interpret_signal.__name__)


@pytest.mark.parametrize("sig, res", [
    (None, 400),
    ("0", 404),
])
def test_interpret_signal_exception(sig, res):
    """
    Testing interpret_signal.
    :return:
    """
    logger.debug("Start of %s function test log.", test_interpret_signal_exception.__name__)

    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()
    # can this be made nicer?
    if sig == None:
        payload = {}
    else:
        payload = {"signal": sig}

    with my_app_instance as client:
        rv = client.post("/", json=payload)
        assert rv.status_code == res
    logger.debug("End of %s function test log.", test_interpret_signal_exception.__name__)
