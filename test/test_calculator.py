# unittest
# part of standard library
# test case by using a subclass called unittest.teastcase
# Multiple methods per test case
# uses assertion methods
# built on j-unit
# looks for test_.... methods and test_..... modules.
# python3 -m unittest test_calculator.py

import unittest
from calculator import Calculator

class TestCalulator(unittest.TestCase):
    
    def test_calculator_class_exists(self):
        calc = Calculator() # attempts to make an object of the class.
        self.assertIsInstance(calc, Calculator) # test to see if object is part of class.

    def test_add_method_exists(self):
        calc = Calculator()
        self.assertTrue(callable(getattr(calc, 'add', None)))

    def test_add_method_accepts_two_inputs(self):
        calc = Calculator()
        self.assertEqual(calc.add(0,0), 0)

    def test_add_method_with_non_numeric_input(self):
        calc = Calculator()
        with self.assertRaisesRegex(TypeError, "Custom Error: Inputs must be numeric"):
            calc.add("a", 5)

    def teat_add_method_returns_numeric(self):
        calc = Calculator()
        self.assertIsInstance(calc.add(1, 2), (int, float))

    def test_add_method_performs_correct_calculations(self):
        calc = Calculator()
        self.assertEqual(calc.add(3, 2), 5)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(0, 0), 0)
        self.assertEqual(calc.add(100, 200), 300)

    @unittest.skip("skipping")
    def test_skip(self):
        pass

    @unittest.skipIf(1 == 1, "no good")
    def test_skipirf(self):
        pass
    








