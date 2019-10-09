import unittest
from Solutions import Lesson03


class FrogJumpTests(unittest.TestCase):
    def test_frog_jump_example_test_01(self):
        x = 10
        y = 85
        d = 30
        res = Lesson03.frog_jmp(x, y, d)
        self.assertEqual(3, res)
