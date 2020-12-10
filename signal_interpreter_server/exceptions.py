"""
Exceptions file.
"""


class ParserGetTitleError(Exception):
    """
    Parsing error.
    """


class WrongFileExtensionError(Exception):
    """
    Wrong file extension error, allowed .json and .xml.
    """


class JsonParserLoadError(Exception):
    """
    JsonParser load_file error: File not found.
    """


# class JsonParserGetTitleError(Exception):
#     """
#     JsonParser load_file error: Signal not found.
#     """


class XmlParserLoadError(Exception):
    """
    XmlParser load_file error: File not found.
    """


# class XmlParserGetTitleError(Exception):
#     """
#     XmlParser load_file error: Signal not found.
#     """
