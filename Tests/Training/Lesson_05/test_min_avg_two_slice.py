import unittest
from Solutions import Lesson05


class MinAvgTwoSliceTests(unittest.TestCase):
    def test_min_avg_two_slice_example_test_01(self):
        a = [4, 2, 2, 5, 1, 5, 8]
        res = Lesson05.min_avg_two_slice(a)
        self.assertEqual(1, res)

    def test_min_avg_two_slice_test_01(self):
        a = [-3, -5, -8, -4, -10]
        res = Lesson05.min_avg_two_slice(a)
        self.assertEqual(2, res)

