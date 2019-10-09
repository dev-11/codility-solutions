import unittest
from Solutions import Lesson09


class Lesson09Tests(unittest.TestCase):
    def test_max_profit_example_test_01(self):
        a = [23171, 21011, 21123, 21366, 21013, 21367]
        res = Lesson09.max_profit(a)
        self.assertEqual(res, 356)

    def test_max_slice_sum_example_test_01(self):
        a = [3, 2, -6, 4, 0]
        res = Lesson09.max_slice_sum(a)
        self.assertEqual(res, 5)

