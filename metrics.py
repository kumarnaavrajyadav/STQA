# modules/metrics.py
def calculate_metrics():
    """Return mock software metrics."""
    metrics = {
        "Lines of Code": 425,
        "Cyclomatic Complexity": 8,
        "Code Coverage (%)": 78.6,
        "Maintainability Index": 72.4
    }
    return {"type": "Metrics", "metrics": metrics}
