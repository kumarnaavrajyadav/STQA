# modules/black_box.py
import json

def run_tests():
    """Run example black-box tests."""
    tests = [
        {"name": "Login validation", "passed": True},
        {"name": "Dashboard rendering", "passed": True},
        {"name": "Data upload", "passed": False},
    ]
    passed = sum(1 for t in tests if t["passed"])
    return {
        "type": "Black Box Testing",
        "total_tests": len(tests),
        "passed": passed,
        "failed": len(tests) - passed,
        "details": tests
    }

def run_custom_test(input_json: str):
    """Run custom JSON-based black-box test."""
    try:
        data = json.loads(input_json)
        func_code = data["function"]
        inputs = data["inputs"]
        expected = data["expected"]

        exec(func_code, globals())
        func_name = func_code.split("(")[0].replace("def ", "").strip()
        results = []

        for i, inp in enumerate(inputs):
            result = eval(f"{func_name}(*{inp})")
            ok = result == expected[i]
            results.append({"input": inp, "output": result, "expected": expected[i], "passed": ok})

        passed = sum(1 for r in results if r["passed"])
        return {"total": len(results), "passed": passed, "failed": len(results) - passed, "results": results}
    except Exception as e:
        return {"error": str(e)}
