import unittest
from Solutions import Lesson10


class Lesson10Tests(unittest.TestCase):
    def test_count_factors_example_test_01():
        n = 24
        res = Lesson10.count_factors(n)
        self.assertEqual(res, 8)

