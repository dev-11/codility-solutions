import unittest
from Solutions import Lesson11


class CountNonDivisibleTest(unittest.TestCase):
    def test_count_non_divisible_example_test_01(self):
        A = [3, 1, 2, 3, 6]
        res = Lesson11.count_non_divisible(A)
        self.assertEqual([2, 4, 3, 2, 0], res)

