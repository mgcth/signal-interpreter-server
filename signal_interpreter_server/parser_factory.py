"""
Factory method class file.
"""


class ParserFactory:
    """
    Factory method class.
    """
    def __init__(self):
        self._parsers = {}
        self._signal_database_format = None

    def set_signal_database_format(self, signal_database_format):
        """
        Set the database format.
        :param signal_database_format:
        :return:
        """
        self._signal_database_format = signal_database_format

    def register_format(self, signal_database_format, parser):
        """
        Register format.
        :param signal_database_format:
        :param parser:
        :return:
        """
        self._parsers[signal_database_format] = parser()

    def get_parser(self):
        """
        Get parser format.
        :return:
        """
        parser = self._parsers.get(self._signal_database_format)
        if not parser:
            raise ValueError(self._signal_database_format)
        return parser
