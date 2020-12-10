# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-12
Current project: signal-interpreter-server


"""
import logging
import json
from signal_interpreter_server.exceptions import JsonParserLoadError, ParserGetTitleError


logger = logging.getLogger(__name__)


class JsonParser:
    """
    Parse JSON object, method for load file and get title from ID.
    """
    def __init__(self):
        self._id_title_pair = {}
        self.data = {}

    def load_file(self, json_file_path):
        """
        Read file.
        :param json_file_path:
        :return:
        """
        try:
            with open(json_file_path) as file:
                self.data = json.load(file)
            logger.info("Loaded database file (JSON): %s", json_file_path)

            self._id_title_pair = {d['id']: d['title'] for d in self.data['services']}
            logger.info("Parsed database file (JSON).")
        except FileNotFoundError as err:
            logger.exception("Exception occurred in file loading (JSON): %s", err)
            raise JsonParserLoadError from err

    def get_signal_title_from_id(self, signal_id: str) -> str:
        """
        Get title from signal id.
        """
        try:
            return self._id_title_pair[signal_id]
        except KeyError as err:
            logger.exception("Exception occurred in file loading (JSON): %s", err)
            raise ParserGetTitleError from err
