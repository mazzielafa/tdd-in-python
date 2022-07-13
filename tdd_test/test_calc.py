import unittest
from calc import Calc

def test_add(self):
        self.assertEqual(CalculatorClass.Calculator.add(10, 5), 15)
        self.assertEqual(CalculatorClass.Calculator.add(-1, 1), 0)
        self.assertEqual(CalculatorClass.Calculator.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(CalculatorClass.Calculator.subtract(10, 5), 5)
        self.assertEqual(CalculatorClass.Calculator.subtract(-1, 1), -2) 
        self.assertEqual(CalculatorClass.Calculator.subtract(-1, -1), 0)


    def test_multiply(self):
        self.assertEqual(CalculatorClass.Calculator.multiply(10, 5), 50)
        self.assertEqual(CalculatorClass.Calculator.multiply(-1, 1), -1)
        self.assertEqual(CalculatorClass.Calculator.multiply(-1, -1), 1)
        
        
if __name__ == '__main__':
    unittest.main
