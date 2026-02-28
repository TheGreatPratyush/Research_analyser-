from flask import Flask, request, jsonify
from main import run_research_pipeline

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "Question required"}), 400

    try:
        report = run_research_pipeline(question)
        return jsonify({"report": report})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)