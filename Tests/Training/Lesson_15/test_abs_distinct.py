import unittest
from Solutions import Lesson15


class AbsDistinctTests(unittest.TestCase):
    def test_abs_distinct_example_test_01(self):
        a = [-5, -3, -1, 0, 3, 6]
        res = Lesson15.abs_distinct(a)
        self.assertEqual(5, res)
