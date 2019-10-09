import unittest
import Lesson16


class TieRopesTests(unittest.TestCase):
    def test_tie_ropes_example_test_01(self):
        K = 4
        A = [1, 2, 3, 4, 1, 1, 3]
        res = Lesson16.tie_ropes(K, A)
        self.assertEqual(3, res)

