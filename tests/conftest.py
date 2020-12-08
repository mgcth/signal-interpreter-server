# conftest.py
import pytest
from signal_interpreter_server.json_parser import JsonParser

@pytest.fixture
def jp_instance():
    jp = JsonParser()
    return jp