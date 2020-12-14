"""
Contains routing methods.
"""
import logging
from flask import Flask, request, abort, jsonify
from signal_interpreter_server.parser_factory import ParserFactory
from signal_interpreter_server.exceptions import ParserGetTitleError


logger = logging.getLogger(__name__)

signal_interpreter_app = Flask(__name__)
generic_parser = ParserFactory()


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """
    POST method.
    :return:
    """
    try:
        data = request.get_json()
        server_parser = generic_parser.get_parser()
        title = server_parser.get_signal_title_from_id(data['signal'])
        logger.info("Client sent signal: %s", data['signal'])
        logger.info("Server responded with title: %s", title)
        return jsonify(title)  # jsonify has nothing with parser to do, it's Flask stuff
    except KeyError as err:
        logger.exception("Exception occurred in POST: %s", err)
        abort(400, description="Bad request")
    except ParserGetTitleError as err:
        logger.warning("Exception occurred in title retrieval: %s", err)
        abort(404, description="Page not found")
