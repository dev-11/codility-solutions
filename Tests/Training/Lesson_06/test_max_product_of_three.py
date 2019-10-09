import unittest
from Solutions import Lesson06


class MaxProductOfThreeTests(unittest.TestCase):
    def test_max_product_of_three_example_test_01(self):
        a = [-3, 1, 2, -2, 5, 6]
        res = Lesson06.max_product_of_three(a)
        self.assertEqual(res, 60)

