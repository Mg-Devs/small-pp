from flask import Flask, abort, request
import re

pattern = re.compile("^[a-zA-Z0-9]{8}$")
app = Flask(__name__)

@app.route("/<hash>", methods=['GET'])
def hash_redirect(hash):
    print(hash)
    if not pattern.match(hash):
        abort(400)
    return f"<p>Hello, World!</p>"

@app.route("/create", methods=['POST'])
def create_hash():
    data = request.json