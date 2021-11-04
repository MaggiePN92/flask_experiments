from flask import Flask, request, jsonify
from error_handling_and_logging.feilhaandtering import InvalidAPIUsage
from error_handling_and_logging.foo import Bar
import logging


app = Flask(__name__)


@app.route("/endpoint", methods=["POST"])
def endpoint():
    req = request.get_data().decode('utf8')
    new_bar = Bar(req)
    response = {**new_bar.get_data()}
    return jsonify(response)


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    return jsonify(e.feil_mld()), e.status_code


if __name__ == "__main__":
    logging.basicConfig(filename="./error.log", level=logging.WARNING)
    app.run()