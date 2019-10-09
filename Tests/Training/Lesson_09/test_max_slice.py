import unittest
from Solutions import Lesson09


class MaxSliceTests(unittest.TestCase):
    def test_max_slice_sum_example_test_01(self):
        a = [3, 2, -6, 4, 0]
        res = Lesson09.max_slice_sum(a)
        self.assertEqual(res, 5)
