from flask import Flask, Response, request
app = Flask(__name__)
import os
import socket


@app.route("/")
def hello():
    output = f"""
        Hello World!\n
        I am running on {socket.gethostname()}\n
        You appear to hail from {request.remote_addr}\n\n
        Environment: {map("=".join, os.environ.items())}\n\n
        Headers: {map("=".join, request.headers.items())}\n
    """
    return Response(output, mimetype='text/plain')

if __name__ == "__main__":
    try:
        port = int(os.getenv("PORT"))
    except TypeError:
        port = None
    app.run(debug=True, port=port)
