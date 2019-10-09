import unittest
from Solutions import Lesson07


class Lesson07Tests(unittest.TestCase):
    def test_brackets_example_test_01(self):
        s = "{[()()]}"
        res = Lesson07.brackets(s)
        self.assertEqual(res, 1)

    def test_brackets_example_test_02(self):
        s = "([)()]"
        res = Lesson07.brackets(s)
        self.assertEqual(res, 0)
