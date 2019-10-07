import unittest
from Solutions import Lesson15


class Lesson15Tests(unittest.TestCase):
    def test_count_distinct_slices_example_01(self):
        m = 6
        a = [3, 4, 5, 5, 2]
        res = Lesson15.count_distinct_slices(m, a)
        self.assertEqual(9, res)
