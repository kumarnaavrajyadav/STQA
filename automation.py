# modules/automation.py
"""
Automation Testing Module
"""

import webbrowser
from modules.black_box import run_tests as run_black_box
from modules.white_box import run_tests as run_white_box
from modules.oo_testing import run_tests as run_oo
from modules.metrics import calculate_metrics

class TestForgeAutomation:
    def run_all_tests(self):
        """Run all test modules together."""
        black = run_black_box()
        white = run_white_box()
        oop = run_oo()
        metrics = calculate_metrics()

        summary = {
            "total_passed": black["passed"] + white["passed"] + oop["passed"],
            "total_failed": black["failed"] + white["failed"] + oop["failed"],
            "modules": 4
        }

        return {
            "summary": summary,
            "results": {
                "black_box": black,
                "white_box": white,
                "oop": oop,
                "metrics": metrics
            }
        }

    def open_link(self, url: str):
        """Open a provided URL in the default browser."""
        if not url or not url.startswith(("http://", "https://")):
            return {"error": "Invalid or missing URL. Include http:// or https://"}
        try:
            webbrowser.open(url)
            return {"status": "success", "message": f"Opened {url} in your default browser."}
        except Exception as e:
            return {"status": "failed", "error": str(e)}
