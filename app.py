# app.py
from flask import Flask, request, jsonify
import tiktoken
app = Flask(__name__)


@app.route("/count_tokens", methods=["POST"])
def count_tokens():
    data = request.get_json()
    text = data.get("text", "")
    model = data.get("model", "gpt-4")
    enc = tiktoken.encoding_for_model(model)
    token_count = len(enc.encode(text))
    return jsonify({"token_count": token_count, "model": model})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
