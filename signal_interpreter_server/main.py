import argparse
from routes import signal_interpreter_app
from json_parser import parsejson

def main():
    args = get_args()
    parsejson.load_file(args.file_path)
    signal_interpreter_app.run()

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file_path", required=True)
    return parser.parse_args()

if __name__ == "__main__":
    main()