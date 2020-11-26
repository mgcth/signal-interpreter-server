"""
Contains routing methods.
"""
import logging
from flask import Flask, request, jsonify, abort
from signal_interpreter_server.json_parser import JsonParser
from signal_interpreter_server.exceptions import JsonParserGetTitleError

logger = logging.getLogger(__name__)

jp = JsonParser()
signal_interpreter_app = Flask(__name__)


@signal_interpreter_app.route("/", methods=["POST"])
def interpret_signal():
    """
    POST method.
    :return:
    """
    try:
        data = request.get_json()
        title = jp.get_signal_title_from_id(data['signal'])
        logger.info("Client sent signal: %s", data['signal'])
        logger.info("Server responded with title: %s", title)
        return jsonify(title)
    except KeyError as err:
        logger.exception("Exception occurred in POST: %s", err)
        abort(400, description="Bad request")
    except JsonParserGetTitleError as err:
        logger.warning("Exception occurred in title retrieval: %s", err)
        abort(404, description="Page not found")
