import unittest
import calculator


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(calculator.add(1, 2), 3)

    def test_subtract_1(self):
        self.assertEqual(calculator.subtract(1, 1), 0)

    if __name__ == "__main__":
        unittest.main()
