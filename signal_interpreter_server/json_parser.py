# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created  at 2020-11-12
Current project: signal-interpreter-server


"""

import json


class JsonParser:  # pylint: disable=missing-class-docstring
    def __init__(self):
        """
        Init
        """
        self.json_data = None
        self._id_title_pair = None

    def load_file(self, json_file_path):
        """
        Load file
        :param json_file_path:
        :return:
        """
        with open(json_file_path) as jfp:
            self.json_data = json.load(jfp)

        self._id_title_pair = {d['id']: d['title'] for d in self.json_data['services']}

    def get_signal_title_from_id(self, signal_id: str) -> str:
        """
        Get signal title from id
        :param signal_id:
        :return:
        """
        return self._id_title_pair.get(signal_id)
