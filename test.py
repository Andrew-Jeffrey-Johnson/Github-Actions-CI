import unittest
import calculator


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(3, 4), 7)

    def test_subtract_1(self):
        self.assertEqual(calculator.subtract(1, 1), 0)
        self.assertEqual(calculator.subtract(8, 4), 4)

    def test_multiply_1(self):
        self.assertEqual(calculator.multiply(2, 2), 4)
        self.assertEqual(calculator.multiply(6, 5), 30)

    def test_divide_1(self):
        self.assertEqual(calculator.divide(3, 3), 1)
        self.assertEqual(calculator.divide(6, 2), 3)

    if __name__ == "__main__":
        unittest.main()
