"""
Exceptions file.
"""

class JsonParserError(Exception):
    """
    JsonParser General error
    """

class JsonParserLoadError(Exception):
    """
    JsonParser load_file error: File not found.
    """



class JsonParserGetTitleError(Exception):
    """
    JsonParser load_file error: Signal not found.
    """
