# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-server


"""
from unittest.mock import patch, mock_open
import json

from signal_interpreter_server.json_parser import JsonParser

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
    '''
    * Create a new file called json_parser.py where you have a function called load_file() which will load the signal database into a dictionary
    '''
    jp = JsonParser()
    jp.load_file("dummy")
    assert jp.json_data["services"][0]["title"] == 'ECU Reset'
    assert jp._id_title_pair.get('27') == "Security Access"
    assert jp._id_title_pair.get('888888') == None


@patch("builtins.open", mock_open(read_data=json.dumps(testJson)))
def test_get_signal_title_from_id():
    '''
    Create another function in json_parser.py which will take the signal ID as input and return the signal title by parsing the dictionary you have loaded
    :return:
    '''
    jp = JsonParser()
    jp.load_file("dummy")
    assert jp.get_signal_title_from_id('11') == 'ECU Reset'
    assert jp.get_signal_title_from_id('27') == 'Security Access'

