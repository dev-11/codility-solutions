import unittest
from Solutions import Lesson10


class Lesson10Tests(unittest.TestCase):
    def test_count_factors_example_test_01(self):
        n = 24
        res = Lesson10.count_factors(n)
        self.assertEqual(8, res)

    def test_min_perimeter_rectangle_example_test_01(self):
        n = 30
        res = Lesson10.min_perimeter_rectangle(n)
        self.assertEqual(22, res)

    def test_min_perimeter_rectangle_test_01(self):
        n = 36
        res = Lesson10.min_perimeter_rectangle(n)
        self.assertEqual(24, res)

