from unittest.mock import patch, mock_open
import pytest
from signal_interpreter_server.json_parser import JsonParser, json

VALID_JSON_DATA = '{ "json" : "This is a JSON" }'
PARSED_JSON_DATA = {"json": "This is a JSON"}


def test_load_file():  # without mocking json.load() for checking that the function loads the JSON-file properly
    with patch("builtins.open", mock_open(read_data=VALID_JSON_DATA)):
        json_parser = JsonParser()
        json_parser.load_file('signal_interpreter_server/signal_database.json')  # right way to give path
        assert json_parser.data == PARSED_JSON_DATA


def test_load_file_by_mocking_json_load():  # with mocking json.load() for checking that it gets called properly
    with patch("builtins.open", mock_open(read_data=VALID_JSON_DATA)) as mock_file_object:
        with patch.object(json, "load", return_value=PARSED_JSON_DATA) as mock_json_load:
            json_parser = JsonParser()
            json_parser.load_file("signal_interpreter_server/signal_database.json")
            mock_json_load.assert_called_with(mock_file_object.return_value)
            assert json_parser.data == PARSED_JSON_DATA


@pytest.mark.parametrize("item, expected_result", [
    ("11", "ECU Reset"),
    ("40", None),
    ("27", "Security Access"),
    ("52", None),
])
def test_get_interpretation(item, expected_result):
    json_parser = JsonParser()
    json_parser.data = {"services": [{"title": "Security Access", "id": "27"},
                                     {"title": "ECU Reset", "id": "11"}]}
    assert json_parser.get_interpretation(item) == expected_result
#   assert json_parser.get_interpretation("11") == "ECU Reset"
