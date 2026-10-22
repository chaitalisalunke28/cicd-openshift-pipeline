
import unittest

from service.app import greet


class TestGreet(unittest.TestCase):
    def test_greet_returns_name(self):
        self.assertEqual(greet("Chaitali"), "Hello, Chaitali!")

    def test_greet_empty_name(self):
        self.assertEqual(greet(""), "Hello, !")


if __name__ == "__main__":
    unittest.main()
