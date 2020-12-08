# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-server


"""
from contextlib import contextmanager
from unittest.mock import patch, mock_open
import json
import pytest
import logging
from signal_interpreter_server.exceptions import JsonParserLoadError, JsonParserGetTitleError


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


# @contextmanager
# def does_not_raise():
#     yield
#
#
# @pytest.mark.parametrize(
#     "example_input, expectation",
#     [
#         ("dummy", does_not_raise()),
#         ("dummy", pytest.raises(JsonParserError))
#     ],
# )
@patch("builtins.open", mock_open(read_data=json.dumps(testJson)))
def test_load_file(jp_instance):
    """
    Testing load_file.
    :param jp_instance:
    :return:
    """
    logger.debug("Start of %s function test log.", test_load_file.__name__)
    jp_instance.load_file("dummy")
    assert jp_instance.json_data["services"][0]["title"] == 'ECU Reset'
    assert jp_instance._id_title_pair.get('27') == "Security Access"
    assert jp_instance._id_title_pair.get('888888') == None
    logger.debug("End of %s function test log.", test_load_file.__name__)


@pytest.mark.parametrize("signal, expected_result", [
    ("11", "ECU Reset"),
    ("27", "Security Access"),
])
@patch("builtins.open", mock_open(read_data=json.dumps(testJson)))
def test_get_signal_title_from_id(jp_instance, signal, expected_result):
    """
    Testing get_signal_title_from_id.
    :param jp_instance:
    :param signal:
    :param expected_result:
    :return:
    """
    logger.debug("Start of %s function test log.", test_get_signal_title_from_id.__name__)
    jp_instance.load_file("dummy")
    assert jp_instance.get_signal_title_from_id(signal) == expected_result
    logger.debug("End of %s function test log.", test_get_signal_title_from_id.__name__)


def test_load_file_exception(jp_instance):
    """
    Testing load_file exception.
    :param jp_instance:
    :return:
    """
    logger.debug("Start of %s function test log.", test_load_file_exception.__name__)
    with pytest.raises(JsonParserLoadError):
        jp_instance.load_file("dummy")
    logger.debug("End of %s function test log.", test_load_file_exception.__name__)


@patch("builtins.open", mock_open(read_data=json.dumps(testJson)))
def test_get_signal_title_from_id_exception(jp_instance):
    """
    Testing get_signal_title_from_id exception.
    :param jp_instance:
    :return:
    """
    logger.debug("Start of %s function test log.", test_get_signal_title_from_id_exception.__name__)
    with pytest.raises(JsonParserGetTitleError):
        jp_instance.load_file("dummy")
        jp_instance.get_signal_title_from_id("0")
    logger.debug("End of %s function test log.", test_get_signal_title_from_id_exception.__name__)
