from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/api/health")
def health():
    return {"status": "ok", "app": "Chappell Family Tree"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5092, debug=False)
