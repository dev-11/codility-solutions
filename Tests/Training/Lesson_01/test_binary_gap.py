import unittest
from Solutions import Lesson01


class BinaryGapTests(unittest.TestCase):
    def test_binary_gap_positive_example_test_01(self):
        n = 1041
        gap = Lesson01.binary_gap(n)
        self.assertEqual(gap, 5)

    def test_binary_gap_positive_example_test_02(self):
        n = 32
        gap = Lesson01.binary_gap(n)
        self.assertEqual(gap, 0)