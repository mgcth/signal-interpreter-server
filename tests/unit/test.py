from unittest.mock import patch, mock_open
from flask import Flask
import sys
import json

from signal_interpreter_server.main import main
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.routes import signal_interpreter_app

# testJson = {"services": [{"title": "ECU Reset", "id": "11"}]}
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
def test_load_file():
    """
    * Create a new file called json_parser.py where you have a function called load_file() which will load
    the signal database into a dictionary
    """
    jp = JsonParser()  # Instance of the class
    jp.load_file("dummy")  # calling the function without a path variable since open is mocked
    assert jp.json_data["services"][0]["title"] == 'ECU Reset'
    assert jp.json_data["services"][1]["title"] == 'Security Access'
    assert jp._id_title_pair.get('27') == "Security Access"
    assert jp._id_title_pair.get('888888') == None


@patch("builtins.open", mock_open(read_data=json.dumps(testJson)))
def test_get_signal_title_from_ID():
    '''
    Create another function in json_parser.py which will take the signal ID as input and return
     the signal title by parsing the dictionary you have loaded :return:
    '''
    jp = JsonParser()
    jp.load_file("dummy")
    assert jp.get_signal_title_from_ID('11') == 'ECU Reset'
    assert jp.get_signal_title_from_ID('27') == 'Security Access'


@patch.object(JsonParser, 'get_signal_title_from_ID', return_value="dummy")
def test_interpret_signal(mock_get_signal_title_from_ID):
    '''
    Rename the function mirror_data() in routes.py to interpret_signal() instead. The function should receive the
    payload in the following format {"signal": "ID"} where ID is of type string. Then it should call the function
    that translates ID to a signal title so it can return the title in JSON-format to the client. :return:
    '''
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    with my_app_instance as client:
        payload = {"signal": "11"}
        rv = client.post("/", json=payload)  # simulates a POST-message
        json_data = rv.get_json()
        assert json_data == "dummy"
        mock_get_signal_title_from_ID.assert_called_with("11")



@patch.object(JsonParser, 'get_signal_title_from_ID', return_value="dummy")
@patch.object(Flask, "run")
@patch.object(JsonParser, "load_file")
def test_main(mock_load_file, mock_run, mock_get_signal_title_from_ID):
    '''
    * Use argparse to make it possible to run main.py with the argument --file_path where you can specify the path to the signal database file
    * Call load_file() during the startup of the server, i.e. when executing main.py
    :param mock_load_file:
    :param mock_run:
    :return:
    '''
    signal_interpreter_app.testing = True
    my_app_instance = signal_interpreter_app.test_client()

    with my_app_instance as client:
        with patch.object(sys, "argv", ["main.main", "--file_path", "./signal_database.json"]):
            main()
            payload = {"signal": "11"}
            client.post("/", json=payload)  # simulates a POST-message
            mock_run.assert_called_once()
            mock_load_file.assert_called_with("./signal_database.json")
