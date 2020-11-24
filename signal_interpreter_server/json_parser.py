# json_parser.py
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
        """
        initiate the class JsonParse
        :return:
        """
        self.data = None

    def load_file(self, file_path):
        """
        Read file from file_path and store in json format
        :return:
        """
        with open(file_path, "r") as json_file:
            self.data = json.load(json_file)

    def get_interpretation(self, identifier):
        """
        interpret "services" and return the title for the called id
        :return:
        """
        for service in self.data["services"]:
            if service["id"] == identifier:
                return service["title"]
        return None
