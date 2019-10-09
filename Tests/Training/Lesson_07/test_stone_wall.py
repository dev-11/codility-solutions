import unittest
from Solutions import Lesson07


class StoneWallTests(unittest.TestCase):
    def test_stone_wall_example_test_01(self):
        h = [8, 8, 5, 7, 9, 8, 4, 8]
        res = Lesson07.stone_wall(h)
        self.assertEqual(7, res)