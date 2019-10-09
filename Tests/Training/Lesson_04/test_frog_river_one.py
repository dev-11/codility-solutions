import unittest
from Solutions import Lesson04


class FrogRiverOneTests(unittest.TestCase):
    def test_frog_river_one_example_test_01(self):
        x = 5
        a = [1, 3, 1, 4, 2, 3, 5, 4]
        res = Lesson04.frog_river_one(x, a)
        self.assertEqual(6, res)
