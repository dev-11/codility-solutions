import unittest
from Solutions import Lesson04


class Lesson04Tests(unittest.TestCase):
    def test_frog_river_one_sample_test_01(self):
        x = 5
        a = [1, 3, 1, 4, 2, 3, 5, 4]
        res = Lesson04.frog_river_one(x, a)
        self.assertEqual(6, res)

    def test_perm_check_sample_test_01(self):
        a = [4, 1, 3, 2]
        res = Lesson04.perm_check(a)
        self.assertEqual(1, res)

    def test_perm_check_sample_test_02(self):
        a = [4, 1, 3]
        res = Lesson04.perm_check(a)
        self.assertEqual(0, res)

    def test_missing_integer_sample_test_01(self):
        a = [1, 3, 6, 4, 1, 2]
        res = Lesson04.missing_integer(a)
        self.assertEqual(res, 5)

    def test_missing_integer_sample_test_02(self):
        a = [1, 2, 3]
        res = Lesson04.missing_integer(a)
        self.assertEqual(res, 4)

    def test_missing_integer_sample_test_03(self):
        a = [-1, -3]
        res = Lesson04.missing_integer(a)
        self.assertEqual(res, 1)
