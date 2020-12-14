"""
Share class instance between tests.
"""
# conftest.py
import pytest
from signal_interpreter_server.parser_factory import ParserFactory
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.xml_parser import XmlParser


@pytest.fixture
def parse_factory_instance():
    """
    Share class instance.
    :return:
    """
    parser_factory = ParserFactory()
    return parser_factory


@pytest.fixture
def json_parser_instance():
    """
    Share class instance.
    :return:
    """
    json_parser = JsonParser()
    return json_parser


@pytest.fixture
def xml_parser_instance():
    """
    Share class instance.
    :return:
    """
    xml_parser = XmlParser()
    return xml_parser
