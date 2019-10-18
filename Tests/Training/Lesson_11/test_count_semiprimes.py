import unittest
from Solutions import Lesson11


class CountSemiprimesTest(unittest.TestCase):
    def test_count_semiprimes_example_test_01(self):
        N = 26
        P = [1, 4, 16]
        Q = [26, 10, 20]
        res = Lesson11.count_semiprimes(N, P, Q)
        self.assertEqual([10, 4, 0], res)
