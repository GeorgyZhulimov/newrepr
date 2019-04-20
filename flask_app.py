from flask import Flask, request
import logging
from alisa_sdk import *
from main_function import *

app = Flask(__name__)
session_storage = {}

@app.route('/')
def hello_world():
    return "Hello World"

@app.route("/", methods = ["POST"])
def main():
    alice_request = AliceRequest
    alice_response = AliceResponse
    logging.info("Request {}".format(alice_request))

    alice_response, session_storage[alice_request.user_id] = handle_dialog(
    alice_request, alice_response, session_storage.get(alice_request.user_id)
    )
    logging.info("Response {}".format(alice_response))
    return alice_response.dumps()

if __name__=='__main__':
    app.run()
