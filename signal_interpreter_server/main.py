"""
Server program.
"""
import argparse
from signal_interpreter_server.routes import signal_interpreter_app, jp


def main():
    """
    Program entry function.
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file_path', help='Specify the path to the signal database file')
    args = parser.parse_args()
    json_path = args.file_path
    jp.load_file(json_path)
    signal_interpreter_app.run()


def init():
    """
    Entry to main. But why not just main()?
    :return:
    """
    if __name__ == "__main__":
        main()


init()
