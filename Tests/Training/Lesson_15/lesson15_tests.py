import unittest
from Solutions import Lesson15


class Lesson15Tests(unittest.TestCase):
    def test_count_distinct_slices_example_01(self):
        m = 6
        a = [3, 4, 5, 5, 2]
        res = Lesson15.count_distinct_slices(m, a)
        self.assertEqual(9, res)

    def test_count_triangles_example_test_01(self):
        a = [10, 2, 5, 1, 8, 12]
        res = Lesson15.count_triangles(a)
        self.assertEqual(4, res)

    def test_count_triangles_test_01(self):
        a = [5, 3, 2]
        res = Lesson15.count_triangles(a)
        self.assertEqual(0, res)

    def test_count_triangles_test_02(self):
        a = [3, 3, 5, 6]
        res = Lesson15.count_triangles(a)
        self.assertEqual(3, res)

    def test_abs_distinct_example_test_01(self):
        a = [-5, -3, -1, 0, 3, 6]
        res = Lesson15.abs_distinct(a)
        self.assertEqual(5, res)

