# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created  at 2020-11-12
Current project: signal-interpreter-server


"""

import json


class JsonParser:

    def __init__(self):
        self.json_data = None
        self._id_title_pair = None

    def load_file(self, jsonFilePath):
        with open(jsonFilePath) as f:
            self.json_data = json.load(f)

        self._id_title_pair = {d['id']: d['title'] for d in self.json_data['services']}

    def get_signal_title_from_ID(self, signal_ID: str) -> str:
        return self._id_title_pair.get(signal_ID)
