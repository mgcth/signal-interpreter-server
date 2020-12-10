"""
Server program.
"""
import os
import argparse
import logging
from signal_interpreter_server.routes import signal_interpreter_app, generic_parser
from signal_interpreter_server.exceptions import WrongFileExtensionError
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.xml_parser import XmlParser


logger = logging.getLogger(__name__)

generic_parser.register_format(".json", JsonParser)
generic_parser.register_format(".xml", XmlParser)


def get_file_path_from_arguments():
    """
    Return the file path given as argument.
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_path', help='Specify the path to the signal database file')
    args = parser.parse_args()
    return args.file_path


def get_file_ending(path):
    """
    Get the file extension from path.
    :param path:
    :return:
    """
    _, file_extension = os.path.splitext(path)
    if file_extension not in (".json", ".xml"):
        raise WrongFileExtensionError

    return file_extension


def main():
    """
    Program entry function.
    :return:
    """
    logger.info("Program started.")

    database_path = get_file_path_from_arguments()

    logger.info("Entered filepath: %s", database_path)

    database_type = get_file_ending(database_path)
    generic_parser.set_signal_database_format(database_type)
    server_parser = generic_parser.get_parser()
    server_parser.load_file(database_path)

    logger.info("Selected parser: %s", server_parser)
    logger.info("Server starts.")

    signal_interpreter_app.run()

    logger.info("Server terminates.")
    logger.info("Program terminated.")


def init():
    """
    Entry to main. But why not just main()?
    :return:
    """
    if __name__ == "__main__":
        main()


init()
