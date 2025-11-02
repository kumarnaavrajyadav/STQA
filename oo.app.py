# test_cases/oo_app.py
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"

class Employee(Person):
    def __init__(self, name, emp_id, salary):
        super().__init__(name)
        self.emp_id = emp_id
        self.salary = salary

    def give_raise(self, amount):
        if amount < 0:
            raise ValueError("Raise must be positive")
        self.salary += amount
        return self.salary

class Department:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, emp):
        if not isinstance(emp, Employee):
            raise TypeError("Only Employee can be a member")
        self.members.append(emp)

    def total_salary(self):
        return sum(m.salary for m in self.members)
