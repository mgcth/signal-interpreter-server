# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-server


"""
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-arguments
import sys
import logging
from unittest.mock import patch
import pytest
from flask import Flask

from signal_interpreter_server.main import main, init, get_file_path_from_arguments, get_file_ending
from signal_interpreter_server.parser_factory import ParserFactory
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.xml_parser import XmlParser
from signal_interpreter_server.routes import signal_interpreter_app
from signal_interpreter_server.exceptions import WrongFileExtensionError


logger = logging.getLogger(__name__)


JSON_TEST_FILE = "data/signal_database.json"
XML_TEST_FILE = "data/signal_database.xml"


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


@patch.object(sys, "argv", ["signal-interpreter-server", "-f", JSON_TEST_FILE])
def test_get_file_path_from_arguments():
    """
    Test the arguments in main.
    :return:
    """
    assert get_file_path_from_arguments() == JSON_TEST_FILE


@patch.object(ParserFactory, 'get_parser')
@patch.object(JsonParser, 'get_signal_title_from_id')
@patch.object(JsonParser, "load_file")
@patch.object(Flask, "run")
@patch("signal_interpreter_server.main.get_file_ending")
@patch("signal_interpreter_server.main.get_file_path_from_arguments")
def test_main_json(
        mock_get_file_path_from_arguments,
        mock_get_file_ending,
        mock_run,
        mock_load_file,
        mock_get_signal_title_from_id,
        mock_get_parser,
        parse_factory_instance,
        json_parser_instance):
    """
    Test main function.
    :param mock_load_file:
    :param mock_run:
    :return:
    """
    logger.debug("End of %s function test log.", test_main_json.__name__)
    parse_factory_instance.register_format(".json", JsonParser)
    parse_factory_instance.set_signal_database_format(".json")  # why mock?
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    mock_get_file_path_from_arguments.return_value = JSON_TEST_FILE
    mock_get_file_ending.return_value = ".json"
    mock_get_parser.return_value = json_parser_instance
    mock_get_signal_title_from_id.return_value = "dummy"

    with my_app_instance as client:
        main()
        payload = {"signal": "11"}
        client.post("/", json=payload)  # simulates a POST-message
        mock_run.assert_called_once()

        mock_load_file.assert_called_with(JSON_TEST_FILE)
    logger.debug("Start of %s function test log.", test_main_json.__name__)


@patch.object(ParserFactory, 'get_parser')
@patch.object(XmlParser, 'get_signal_title_from_id')
@patch.object(XmlParser, "load_file")
@patch.object(Flask, "run")
@patch("signal_interpreter_server.main.get_file_ending")
@patch("signal_interpreter_server.main.get_file_path_from_arguments")
def test_main_xml(
        mock_get_file_path_from_arguments,
        mock_get_file_ending,
        mock_run,
        mock_load_file,
        mock_get_signal_title_from_id,
        mock_get_parser,
        parse_factory_instance,
        xml_parser_instance):
    """
    Test main function.
    :param mock_load_file:
    :param mock_run:
    :return:
    """
    logger.debug("End of %s function test log.", test_main_xml.__name__)
    parse_factory_instance.register_format(".xml", XmlParser)
    parse_factory_instance.set_signal_database_format(".xml")  # why mock?
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    mock_get_file_path_from_arguments.return_value = XML_TEST_FILE
    mock_get_file_ending.return_value = ".xml"
    mock_get_parser.return_value = xml_parser_instance
    mock_get_signal_title_from_id.return_value = "dummy"

    with my_app_instance as client:
        main()
        payload = {"signal": "11"}
        client.post("/", json=payload)  # simulates a POST-message
        mock_run.assert_called_once()

        mock_load_file.assert_called_with(XML_TEST_FILE)
    logger.debug("Start of %s function test log.", test_main_xml.__name__)


@pytest.mark.parametrize("path, extension", [
    ("dummy.json", ".json"),
    ("dummy.xml", ".xml")
])
def test_get_file_ending(path, extension):
    """
    Test the arguments in main.
    :return:
    """
    logger.debug("Start of %s function test log.", test_get_file_ending.__name__)
    assert get_file_ending(path) == extension
    logger.debug("End of %s function test log.", test_get_file_ending.__name__)


def test_get_file_ending_exception():
    """
    Test the arguments in main.
    :return:
    """
    logger.debug("Start of %s function test log.", test_get_file_ending_exception.__name__)
    with pytest.raises(WrongFileExtensionError):
        get_file_ending("dummy.lol")
    logger.debug("End of %s function test log.", test_get_file_ending_exception.__name__)
