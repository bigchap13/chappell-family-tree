from flask import Flask, jsonify, render_template
from pathlib import Path
import json

app = Flask(__name__)


DATA_FILE = Path(__file__).parent / "data" / "family_history.json"


def load_family_history():
    return json.loads(DATA_FILE.read_text())


@app.get("/")
def home():
    return render_template("index.html", research=load_family_history())


@app.get("/api/research")
def research():
    return jsonify(load_family_history())


@app.get("/api/health")
def health():
    return {"status": "ok", "app": "Chappell Family Tree"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5092, debug=False)
