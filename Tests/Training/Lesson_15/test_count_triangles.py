import unittest
from Solutions import Lesson15


class CountTrianglesTests(unittest.TestCase):
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
