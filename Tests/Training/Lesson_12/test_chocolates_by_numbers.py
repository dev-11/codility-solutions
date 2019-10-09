import unittest
from Solutions import Lesson12


class ChocolatesByNumbersTests(unittest.TestCase):
    def test_chocolates_by_numbers_example_test_01(self):
        N = 10
        M = 4
        res = Lesson12.chocolates_by_numbers(N, M)
        self.assertEqual(5, res)
