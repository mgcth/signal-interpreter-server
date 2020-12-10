# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-12
Current project: signal-interpreter-server


"""
import logging
import xml.etree.ElementTree as ET
import xmltodict
from signal_interpreter_server.exceptions import XmlParserLoadError, ParserGetTitleError


logger = logging.getLogger(__name__)


class XmlParser:
    """
    Parse XML object, method for load file and get title from ID.
    """
    def __init__(self):
        self._id_title_pair = {}
        self.data = {}

    def load_file(self, xml_file_path):
        """
        Read file.
        :param xml_file_path:
        :return:
        """
        try:
            tree = ET.parse(xml_file_path)
            data = tree.getroot()
            xml_string = ET.tostring(data, encoding="utf-8", method="xml")
            self.data = dict(xmltodict.parse(xml_string))
            logger.info("Loaded database file (XML): %s", xml_file_path)

            self._id_title_pair = {d["@id"]: d["title"] for d in self.data["services"]["service"]}
            logger.info("Parsed database file (XML).")
        except FileNotFoundError as err:
            logger.exception("Exception occurred in file loading (XML): %s", err)
            raise XmlParserLoadError from err

    def get_signal_title_from_id(self, signal_id: str) -> str:
        """
        Get title from signal id.
        """
        try:
            return self._id_title_pair[signal_id]
        except KeyError as err:
            logger.exception("Exception occurred in file loading (XML): %s", err)
            raise ParserGetTitleError from err
