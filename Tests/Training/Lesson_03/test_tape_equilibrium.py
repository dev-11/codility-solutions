import unittest
from Solutions import Lesson03


class TapeEquilibriumTests(unittest.TestCase):
    def test_tape_equilibrium_example_test_01(self):
        a = [3, 1, 2, 4, 3]
        res = Lesson03.tape_equilibrium(a)
        self.assertEqual(1, res)
