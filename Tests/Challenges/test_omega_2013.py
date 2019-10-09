import unittest
from Solutions import Challenges


class Omega2013Tests(unittest.TestCase):
    def test_omega_2013_example_test_01(self):
        a = [5, 6, 4, 3, 6, 2, 3]
        b = [2, 3, 5, 2, 4]
        res = Challenges.omega_2013(a, b)
        self.assertEqual(4, res)
