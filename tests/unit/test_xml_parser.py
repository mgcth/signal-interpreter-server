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
from signal_interpreter_server.xml_parser import XmlParser
from signal_interpreter_server.exceptions import XmlParserLoadError, ParserGetTitleError


logger = logging.getLogger(__name__)


TEST_XML = "<services>\n\t<service id=\"11\"><title>ECU Reset</title></service>\n\t" \
           "<service id=\"27\"><title>Security Access</title></service>\n</services>"


def test_load_file(xml_parser_instance):
    """
    Test XML load file.
    :param xml_parser_instance:
    :return:
    """
    logger.debug("Start of %s function test log.", test_load_file.__name__)
    with patch("xml.etree.ElementTree.parse") as mock_parse:
        with patch("xml.etree.ElementTree.tostring") as mock_to_string:
            mock_to_string.return_value = TEST_XML
            xml_parser_instance.load_file("path_to_file")
            mock_parse.assert_called_with("path_to_file")
            mock_to_string.assert_called_once()
    logger.debug("Start of %s function test log.", test_load_file.__name__)


@pytest.mark.parametrize("signal, expected_result", [
    ("11", "ECU Reset"),
    ("27", "Security Access"),
])
@patch.object(XmlParser, "get_signal_title_from_id")
def test_get_signal_title_from_id(mock_get_signal_title_from_id, signal, expected_result, xml_parser_instance):
    """
    Test XML get signal from title.
    :param xml_parser_instance:
    :return:
    """
    logger.debug("Start of %s function test log.", test_get_signal_title_from_id.__name__)
    mock_get_signal_title_from_id.return_value = expected_result
    assert xml_parser_instance.get_signal_title_from_id(signal) == expected_result
    logger.debug("Start of %s function test log.", test_get_signal_title_from_id.__name__)


def test_load_file_exception(xml_parser_instance):
    """
    Testing load_file exception.
    :param xml_parser_instance:
    :return:
    """
    logger.debug("Start of %s function test log.", test_load_file_exception.__name__)
    with pytest.raises(XmlParserLoadError):
        xml_parser_instance.load_file("dummy")
    logger.debug("End of %s function test log.", test_load_file_exception.__name__)


def test_get_signal_title_from_id_exception(xml_parser_instance):
    """
    Testing get_signal_title_from_id exception.
    :param xml_parser_instance:
    :return:
    """
    logger.debug("Start of %s function test log.", test_get_signal_title_from_id_exception.__name__)
    with pytest.raises(ParserGetTitleError):
        xml_parser_instance.get_signal_title_from_id("0")
    logger.debug("End of %s function test log.", test_get_signal_title_from_id_exception.__name__)
