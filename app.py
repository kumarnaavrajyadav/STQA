# app.py
from flask import Flask, render_template, jsonify, request
from modules.black_box import run_tests as run_black_box_tests, run_custom_test
from modules.white_box import run_tests as run_white_box_tests, run_custom_code
from modules.oo_testing import run_tests as run_oo_tests
from modules.metrics import calculate_metrics
from modules.automation import TestForgeAutomation
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    automation = TestForgeAutomation()
    results = automation.run_all_tests()
    summary = results["summary"]
    return render_template("dashboard.html", results=results, summary=summary)

@app.route("/api/run_all")
def api_run_all():
    automation = TestForgeAutomation()
    results = automation.run_all_tests()
    return jsonify(results)

@app.route("/api/white_box", methods=["POST"])
def api_white_box():
    code = request.form.get("code", "")
    result = run_custom_code(code)
    return jsonify(result)

@app.route("/api/black_box", methods=["POST"])
def api_black_box():
    data = request.form.get("data", "")
    result = run_custom_test(data)
    return jsonify(result)

@app.route("/api/oop")
def api_oop():
    return jsonify(run_oo_tests())

@app.route("/api/metrics")
def api_metrics():
    return jsonify(calculate_metrics())

@app.route("/api/automation", methods=["POST"])
def api_automation():
    """Run automation and open the provided URL."""
    url = request.form.get("url", "")
    automation = TestForgeAutomation()
    result = automation.open_link(url)
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\n🧪 TestForge running on http://127.0.0.1:{port}")
    app.run(debug=True, port=port)
