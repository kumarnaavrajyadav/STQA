# test_cases/test_oo_app.py
import unittest
from oo_app import Person, Employee, Department

class TestPerson(unittest.TestCase):
    def test_greet(self):
        p = Person("Alice")
        self.assertEqual(p.greet(), "Hello, Alice")

class TestEmployee(unittest.TestCase):
    def test_salary_raise(self):
        e = Employee("Bob", 1001, 5000)
        new_sal = e.give_raise(500)
        self.assertEqual(new_sal, 5500)
    def test_salary_raise_negative(self):
        e = Employee("Bob", 1001, 5000)
        with self.assertRaises(ValueError):
            e.give_raise(-100)

class TestDepartment(unittest.TestCase):
    def test_add_member_and_total(self):
        d = Department("Dev")
        e1 = Employee("E1", 101, 3000)
        e2 = Employee("E2", 102, 4000)
        d.add_member(e1)
        d.add_member(e2)
        self.assertEqual(d.total_salary(), 7000)
    def test_add_member_type_check(self):
        d = Department("Dev")
        with self.assertRaises(TypeError):
            d.add_member("not_an_employee")

if __name__ == "__main__":
    unittest.main()
