import unittest
from Solutions import Lesson05


class Lesson05Tests(unittest.TestCase):
    def test_passing_cars_example_test_01(self):
        a = [0, 1, 0, 1, 1]
        res = Lesson05.passing_cars(a)
        self.assertEqual(5, res)

    def test_genomic_range_query_example_test_01(self):
        s = 'CAGCCTA'
        p = [2, 5, 0]
        q = [4, 5, 6]
        res = Lesson05.genomic_range_query(s, p, q)
        self.assertEqual([2, 4, 1], res)
