import unittest
from employee import Employee

class EmployeeTest(unittest.TestCase):
    def add_Employee(self):
        new_emp = Employee("Jane", "j@j.com", "user1", "x1234x")
        self.assertIsNotNone(new_emp)
        message = new_emp()
        print(message)