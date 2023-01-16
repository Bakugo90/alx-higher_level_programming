import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calc.addition(10, 5), 15)

    def test_division(self):
        self.assertEqual(calc.division(10, 2), 5)
        self.assertRaises(ValueError, calc.division, 10, 0)

if __name__ == "__main__":
    unittest.main()

