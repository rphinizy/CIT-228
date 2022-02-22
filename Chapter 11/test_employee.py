import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Unit Tests for the Employee class """
    
    def setUp(self):
        first_name="Steve"
        last_name="Guy"
        salary=40000
        self.employee = Employee(first_name, last_name,salary)
    
    def test_give_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary,45000)
    
    def test_give__custom_raise(self):
        self.employee.give_raise(20000)
        self.assertEqual(self.employee.salary,60000)


if __name__ == '__main__':
    unittest.main()


