import unittest
from Solutions import Lesson06


class DistinctTests(unittest.TestCase):

    def test_distinct_example_test_01(self):
        a = [2, 1, 1, 2, 3, 1]
        res = Lesson06.distinct(a)
        self.assertEqual(res, 3)

