from routes import signal_interpreter_app, jp
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', help='Specify the path to the signal database file')
    args = parser.parse_args()
    jsonPath = args.file_path
    jp.load_file(jsonPath)
    signal_interpreter_app.run()

if __name__ == "__main__":
    main()


