from flask import Flask, jsonify, request

server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World"

if __name__ == "__main__":
    server.run()