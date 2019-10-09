import unittest
from Solutions import Lesson05


class GenomicRangeQueryTests(unittest.TestCase):
    def test_genomic_range_query_example_test_01(self):
        s = 'CAGCCTA'
        p = [2, 5, 0]
        q = [4, 5, 6]
        res = Lesson05.genomic_range_query(s, p, q)
        self.assertEqual([2, 4, 1], res)

