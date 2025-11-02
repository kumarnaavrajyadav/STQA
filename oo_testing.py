# modules/oo_testing.py
class Sample:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y

def run_tests():
    """Run sample OOP tests."""
    s1 = Sample(2, 3)
    s2 = Sample(-1, 1)
    results = [
        {"test": "Addition positive", "expected": 5, "got": s1.add(), "passed": s1.add() == 5},
        {"test": "Addition with negative", "expected": 0, "got": s2.add(), "passed": s2.add() == 0},
    ]
    passed = sum(1 for t in results if t["passed"])
    return {"type": "OOP Testing", "total": len(results), "passed": passed, "failed": len(results) - passed, "details": results}
