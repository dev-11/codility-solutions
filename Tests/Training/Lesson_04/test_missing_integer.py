import unittest
from Solutions import Lesson04


class MissingIntegerTests(unittest.TestCase):
    def test_missing_integer_example_test_01(self):
        a = [1, 3, 6, 4, 1, 2]
        res = Lesson04.missing_integer(a)
        self.assertEqual(5, res)

    def test_missing_integer_example_test_02(self):
        a = [1, 2, 3]
        res = Lesson04.missing_integer(a)
        self.assertEqual(4, res)

    def test_missing_integer_example_test_03(self):
        a = [-1, -3]
        res = Lesson04.missing_integer(a)
        self.assertEqual(1, res)

    def test_missing_integer_test_01(self):
        a = [4, 5, 6, 2]
        res = Lesson04.missing_integer(a)
        self.assertEqual(1, res)
