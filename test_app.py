
import unittest
from app import add


class TestApp(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(10, 20), 30)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_add_zero(self):
        self.assertEqual(add(10, 0), 10)


if __name__ == "__main__":
    unittest.main()
