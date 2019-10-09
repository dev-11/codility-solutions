import unittest
from Solutions import Lesson07


class NestingTests(unittest.TestCase):
    def test_nesting_example_test_01(self):
        s = "(()(())())"
        res = Lesson07.nesting(s)
        self.assertEqual(res, 1)

    def test_nesting_example_test_02(self):
        s = "())"
        res = Lesson07.nesting(s)
        self.assertEqual(res, 0)
