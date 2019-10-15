import unittest
from Solutions import Lesson05


class CountDivTests(unittest.TestCase):
    def test_count_div_example_test_01(self):
        a = 6
        b = 11
        k = 2
        res = Lesson05.count_div(a, b, k)
        self.assertEqual(3, res)

    def test_count_div_test_01(self):
        a = 0
        b = 0
        k = 11
        res = Lesson05.count_div(a, b, k)
        self.assertEqual(1, res)
