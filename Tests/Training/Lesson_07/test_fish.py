import unittest
from Solutions import Lesson07


class FishTests(unittest.TestCase):
    def test_fish_example_test_01(self):
        A = [4, 3, 2, 1, 5]
        B = [0, 1, 0, 0, 0]
        res = Lesson07.fish(A, B)
        self.assertEqual(res, 2)
