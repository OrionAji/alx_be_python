import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        
        self.calc = SimpleCalculator()

    def test_addition(self):
        
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(1,-2), -1)
        self.assertEqual(self.calc.add(0,-2), -2)
        # Add more assertions to thoroughly test the add method.
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 4), 1)
        self.assertEqual(self.calc.subtract(-3, 2), -5)
        self.assertEqual(self.calc.subtract(5, -2), 7)
        self.assertEqual(self.calc.subtract(0, 4), -4)
        self.assertEqual(self.calc.subtract(0, 3), -3)
        
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 2), 0)
        self.assertEqual(self.calc.multiply(-1, 4), -4)
        self.assertEqual(self.calc.multiply(0.5, 4), 2)
        self.assertEqual(self.calc.multiply(1, 4), 4)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(0, 2), 0)
        self.assertEqual(self.calc.divide(1, 2), 0.5)
        self.assertEqual(self.calc.divide(2, 0), ZeroDivisionError)
        