import unittest
from Solutions import Lesson03


class Lesson03Tests(unittest.TestCase):
    def test_from_jump_sample_test_01(self):
        x = 10
        y = 85
        d = 30
        res = Lesson03.frog_jmp(x, y, d)
        self.assertEqual(3, res)

    def test_perm_missing_elem(self):
        a = [2, 3, 1, 5]
        res = Lesson03.perm_missing_elem(a)
        self.assertEqual(4, res)

    def test_tape_equilibrium(self):
        a = [3, 1, 2, 4, 3]
        res = Lesson03.tape_equilibrium(a)
        self.assertEqual(1, res)
