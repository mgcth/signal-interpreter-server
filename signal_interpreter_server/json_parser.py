# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created  at 2020-11-12
Current project: signal-interpreter-server


"""

import json


class JsonParser:
    """
    Parse JSON object, method for load file and get title from ID.
    """
    def __init__(self):
        self._id_title_pair = {}
        self.json_data = {}

    def load_file(self, json_file_path):
        """
        Read file.
        :param json_file_path:
        :return:
        """
        with open(json_file_path) as file:
            self.json_data = json.load(file)

        self._id_title_pair = {d['id']: d['title'] for d in self.json_data['services']}

    def get_signal_title_from_id(self, signal_id: str) -> str:
        """
        Get title from signal id.
        """
        return self._id_title_pair.get(signal_id)
