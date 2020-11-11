import json
import os
from flask import jsonify

# can be circumvented by giving full path, but use this instead
path = os.getcwd().split("\\")
path = "\\".join(path[:-1]) + "\\"

class ParseJSON:
    def __init__(self):
        self.data = {}

    def load_file(self, fpath):
        with open(path + fpath) as f:
            self.data = json.load(f)

    def get_signal_title(self, id):
        for s in self.data["services"]:
            if s["id"] == id:
                return jsonify(s["title"])

# instantiate class for json parsing
parsejson = ParseJSON()