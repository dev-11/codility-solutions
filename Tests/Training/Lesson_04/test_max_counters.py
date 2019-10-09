import unittest
from Solutions import Lesson04


class MaxCountersTests(unittest.TestCase):
    def test_max_counters_example_test_01(self):
        N = 5
        A = [3, 4, 4, 6, 1, 4, 4]
        res = Lesson04.max_counters(N, A)
        self.assertEqual([3, 2, 2, 4, 2], res)
