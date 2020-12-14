# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-server


"""
# pylint: disable=missing-function-docstring
import logging
from unittest.mock import patch
import pytest
from signal_interpreter_server.parser_factory import ParserFactory
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.xml_parser import XmlParser
from signal_interpreter_server.routes import signal_interpreter_app


logger = logging.getLogger(__name__)


@pytest.mark.parametrize("sig", [
    "11",
    "27",
])
@patch.object(ParserFactory, 'get_parser')
@patch.object(JsonParser, 'get_signal_title_from_id', return_value="dummy")
def test_interpret_signal_json(mock_get_signal_title_from_id, mock_get_parser, sig, json_parser_instance):
    """
    Testing interpret_signal.
    :param mock_get_signal_title_from_id:
    :param sig:
    :return:
    """
    logger.debug("Start of %s function test log.", test_interpret_signal_json.__name__)
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()
    payload = {"signal": sig}

    mock_get_parser.return_value = json_parser_instance

    with my_app_instance as client:
        response_value = client.post("/", json=payload)  # simulates a POST-message
        json_data = response_value.get_json()
        assert json_data == "dummy"
        mock_get_signal_title_from_id.assert_called_with(sig)
    logger.debug("End of %s function test log.", test_interpret_signal_json.__name__)


@pytest.mark.parametrize("sig", [
    "11",
    "27",
])
@patch.object(ParserFactory, 'get_parser')
@patch.object(XmlParser, 'get_signal_title_from_id', return_value="dummy")
def test_interpret_signal_xml(mock_get_signal_title_from_id, mock_get_parser, sig, xml_parser_instance):
    """
    Testing interpret_signal.
    :param mock_get_signal_title_from_id:
    :param sig:
    :return:
    """
    logger.debug("Start of %s function test log.", test_interpret_signal_xml.__name__)
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()
    payload = {"signal": sig}

    mock_get_parser.return_value = xml_parser_instance

    with my_app_instance as client:
        response_value = client.post("/", json=payload)  # simulates a POST-message
        json_data = response_value.get_json()
        assert json_data == "dummy"
        mock_get_signal_title_from_id.assert_called_with(sig)
    logger.debug("End of %s function test log.", test_interpret_signal_xml.__name__)


@pytest.mark.parametrize("res, payload", [
    (400, {}),
    (404, {"signal": "0"}),
])
@patch.object(ParserFactory, 'get_parser')
def test_interpret_signal_exception(mock_get_parser, res, payload, json_parser_instance):
    """
    Testing interpret_signal.
    :return:
    """
    logger.debug("Start of %s function test log.", test_interpret_signal_exception.__name__)
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    mock_get_parser.return_value = json_parser_instance

    with my_app_instance as client:
        response_value = client.post("/", json=payload)
        assert response_value.status_code == res
    logger.debug("End of %s function test log.", test_interpret_signal_exception.__name__)
