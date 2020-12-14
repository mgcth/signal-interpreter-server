# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-server


"""
# pylint: disable=missing-function-docstring
import logging
from unittest.mock import patch, mock_open
import json
import pytest
from signal_interpreter_server.exceptions import JsonParserLoadError, ParserGetTitleError


logger = logging.getLogger(__name__)


testJson = {
    "services": [
        {
            "title": "ECU Reset",
            "id": "11"
        },
        {
            "title": "Security Access",
            "id": "27"
        }
    ]
}


@patch("builtins.open", mock_open(read_data=json.dumps(testJson)))
def test_load_file(json_parser_instance):
    """
    Testing load_file.
    :param jason_parser_instance:
    :return:
    """
    logger.debug("Start of %s function test log.", test_load_file.__name__)
    json_parser_instance.load_file("dummy")
    assert json_parser_instance.data["services"][0]["title"] == 'ECU Reset'
    logger.debug("End of %s function test log.", test_load_file.__name__)


@pytest.mark.parametrize("signal, expected_result", [
    ("11", "ECU Reset"),
    ("27", "Security Access"),
])
@patch("builtins.open", mock_open(read_data=json.dumps(testJson)))
def test_get_signal_title_from_id(json_parser_instance, signal, expected_result):
    """
    Testing get_signal_title_from_id.
    :param jason_parser_instance:
    :param signal:
    :param expected_result:
    :return:
    """
    logger.debug("Start of %s function test log.", test_get_signal_title_from_id.__name__)
    json_parser_instance.load_file("dummy")
    assert json_parser_instance.get_signal_title_from_id(signal) == expected_result
    logger.debug("End of %s function test log.", test_get_signal_title_from_id.__name__)


def test_load_file_exception(json_parser_instance):
    """
    Testing load_file exception.
    :param jason_parser_instance:
    :return:
    """
    logger.debug("Start of %s function test log.", test_load_file_exception.__name__)
    with pytest.raises(JsonParserLoadError):
        json_parser_instance.load_file("dummy")
    logger.debug("End of %s function test log.", test_load_file_exception.__name__)


@patch("builtins.open", mock_open(read_data=json.dumps(testJson)))
def test_get_signal_title_from_id_exception(json_parser_instance):
    """
    Testing get_signal_title_from_id exception.
    :param jason_parser_instance:
    :return:
    """
    logger.debug("Start of %s function test log.", test_get_signal_title_from_id_exception.__name__)
    with pytest.raises(ParserGetTitleError):
        json_parser_instance.load_file("dummy")
        json_parser_instance.get_signal_title_from_id("0")
    logger.debug("End of %s function test log.", test_get_signal_title_from_id_exception.__name__)
