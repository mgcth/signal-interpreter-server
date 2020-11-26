"""
Server program.
"""
import argparse
import logging
from signal_interpreter_server.routes import signal_interpreter_app, jp


logger = logging.getLogger(__name__)


def main():
    """
    Program entry function.
    :return:
    """
    logger.info("Program started.")
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_path', help='Specify the path to the signal database file')
    args = parser.parse_args()
    json_path = args.file_path
    logger.info("Entered filepath: %s", json_path)
    jp.load_file(json_path)
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
