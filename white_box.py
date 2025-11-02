# modules/white_box.py
def run_tests():
    """Run example white-box tests."""
    tests = [
        {"name": "Condition coverage", "passed": True},
        {"name": "Loop coverage", "passed": False},
        {"name": "Statement coverage", "passed": True},
    ]
    passed = sum(1 for t in tests if t["passed"])
    return {
        "type": "White Box Testing",
        "total_tests": len(tests),
        "passed": passed,
        "failed": len(tests) - passed,
        "details": tests
    }

def run_custom_code(code: str):
    """Execute custom code provided by user."""
    try:
        exec(code, globals())
        return {"status": "Code executed successfully"}
    except Exception as e:
        return {"error": str(e)}
