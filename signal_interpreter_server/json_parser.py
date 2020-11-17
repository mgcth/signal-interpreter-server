# json_parser.py
import json


class JsonParser:

    def load_file(self, jsonFilePath):
        with open(jsonFilePath) as f:
            self.json_data = json.load(f)
            self._id_title_pair = {d['id']: d['title'] for d in self.json_data['services']}

    def get_signal_title_from_ID(self, signal_ID: str) -> str:
        return self._id_title_pair.get(signal_ID)
