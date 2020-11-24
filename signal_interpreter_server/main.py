# python -m signal_interpreter_server.main -f signal_interpreter_server/signal_database.json
"""
Server program.
"""
from argparse import ArgumentParser
from signal_interpreter_server.routes import signal_interpreter_app, json_parser


def parse_arguments():
    """
    Argument Parser file path.
    :return:
    """
    parser = ArgumentParser(description="Interpret signal using signal database")
    parser.add_argument("-f", "--file_path", required=True, help="path to signal database file")
    return parser.parse_args()


def main():
    """
    Program entry point.
    :return:
    """
    args = parse_arguments()
    json_parser.load_file(args.file_path)
    signal_interpreter_app.run()


def init():
    """
    Entry to main. increase the code-cov by allowing to write a unit function
    :return:
    """
    if __name__ == "__main__":
        main()


init()
