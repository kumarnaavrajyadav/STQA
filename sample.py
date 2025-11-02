import unittest

class TestLoginFunction(unittest.TestCase):
    def test_valid_login(self):
        self.assertEqual(login("admin", "admin123"), True)
    
    def test_invalid_login(self):
        self.assertEqual(login("user", "wrongpass"), False)

def login(username, password):
    return username == "admin" and password == "admin123"

if __name__ == "__main__":
    unittest.main()
