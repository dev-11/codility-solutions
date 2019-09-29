import unittest
from Solutions import Lesson09


class Lesson09Tests(unittest.TestCase):
    def test_max_profit_test_01(self):
        a = [23171, 21011, 21123, 21366, 21013, 21367]
        res = Lesson09.max_profit(a)
        self.assertIn(res, 356)
