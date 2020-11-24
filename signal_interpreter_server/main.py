# -*- coding: utf-8 -*-
"""
DESCRIPTION

Created at 2020-11-17
Current project: signal-interpreter-server


"""
import argparse
from routes import signal_interpreter_app, jp



def main():
    """
    Main
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', help='Specify the path to the signal database file')
    args = parser.parse_args()
    json_path = args.file_path
    jp.load_file(json_path)
    signal_interpreter_app.run()


if __name__ == "__main__":
    main()
