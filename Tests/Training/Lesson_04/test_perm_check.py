import unittest
from Solutions import Lesson04


class PermCheckTests(unittest.TestCase):
    def test_perm_check_example_test_01(self):
        a = [4, 1, 3, 2]
        res = Lesson04.perm_check(a)
        self.assertEqual(1, res)

    def test_perm_check_example_test_02(self):
        a = [4, 1, 3]
        res = Lesson04.perm_check(a)
        self.assertEqual(0, res)
