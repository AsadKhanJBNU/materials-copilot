"""
Flask web app for Materials Copilot — chat-based UI powered by an LLM.
"""
import os

from flask import Flask, request, jsonify, render_template

from llm_interface import LLMInterface

app = Flask(__name__)

_llm = None


def get_llm():
    global _llm
    if _llm is None:
        _llm = LLMInterface()
    return _llm


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/prompt", methods=["POST"])
def prompt():
    """Accept JSON: prompt (string). Return LLM response as JSON."""
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    data = request.get_json() or {}
    prompt_text = (data.get("prompt") or "").strip()

    if not prompt_text:
        return jsonify({"error": "Missing or empty 'prompt'"}), 400

    try:
        llm = get_llm()
    except ValueError as e:
        return jsonify({"error": "LLM not available.", "details": str(e)}), 503

    try:
        response_text = llm.generate(prompt_text)
        return jsonify({"response": response_text}), 200
    except Exception as e:
        return jsonify({
            "error": "Prompt failed.",
            "details": str(e),
        }), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
