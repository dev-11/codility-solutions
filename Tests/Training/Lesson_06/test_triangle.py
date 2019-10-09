import unittest
from Solutions import Lesson06


class TriangleTests(unittest.TestCase):
    def test_triangle_example_test_01(self):
        a = [10, 2, 5, 1, 8, 20]
        res = Lesson06.triangle(a)
        self.assertEqual(res, 1)

    def test_triangle_example_test_02(self):
        a = [10, 2, 5, 1]
        res = Lesson06.triangle(a)
        self.assertEqual(res, 0)
