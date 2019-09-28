import unittest
from Solutions import Lesson07


class Lesson07Tests(unittest.TestCase):
    def test_brackets_sample_test_01(self):
        s = "{[()()]}"
        res = Lesson07.brackets(s)
        self.assertEqual(res, 1)

    def test_brackets_sample_test_02(self):
        s = "([)()]"
        res = Lesson07.brackets(s)
        self.assertEqual(res, 0)

    def test_nesting_sample_test_01(self):
        s = "(()(())())"
        res = Lesson07.nesting(s)
        self.assertEqual(res, 1)

    def test_nesting_sample_test_02(self):
        s = "())"
        res = Lesson07.nesting(s)
        self.assertEqual(res, 0)

    def test_stone_wall_sample_test01(self):
        h = [8, 8, 5, 7, 9, 8, 4, 8]
        res = Lesson07.stone_wall(h)
        self.assertEqual(7, res)

