import unittest
from Solutions import Lesson06


class Lesson06Tests(unittest.TestCase):
    def test_max_product_of_three_test_01(self):
        a = [-3, 1, 2, -2, 5, 6]
        res = Lesson06.max_product_of_three(a)
        self.assertEqual(res, 60)

    def test_distinct_test_01(self):
        a = [2, 1, 1, 2, 3, 1]
        res = Lesson06.distinct(a)
        self.assertEqual(res, 3)

    def test_triangle_test_01(self):
        a = [10, 2, 5, 1, 8, 20]
        res = Lesson06.triangle(a)
        self.assertEqual(res, 1)

    def test_triangle_test_02(self):
        a = [10, 2, 5, 1]
        res = Lesson06.triangle(a)
        self.assertEqual(res, 0)
