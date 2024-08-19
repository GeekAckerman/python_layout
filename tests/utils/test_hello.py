import unittest
from unittest import TestCase
from python_layout.utils.hello import hello


class TestHello(TestCase):
    def test_hello(self):
        """Test hello"""
        hello("Python3")


if __name__ == "__main__":
    unittest.main()
