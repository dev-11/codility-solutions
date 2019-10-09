import unittest
from Solutions import Lesson10


class CountFactorsTests(unittest.TestCase):
    def test_count_factors_example_test_01(self):
        n = 24
        res = Lesson10.count_factors(n)
        self.assertEqual(8, res)
