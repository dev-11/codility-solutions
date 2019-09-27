import unittest
from Solutions import *


class Lesson01Tests(unittest.TestCase):
    def test_binary_gap_positive_sample_test_01(self):
        n = 1041
        gap = Lesson01.binary_gap(n)
        self.assertEqual(gap, 5)

    def test_binary_gap_positive_sample_test_02(self):
        n = 32
        gap = Lesson01.binary_gap(n)
        self.assertEqual(gap, 0)


class Lesson02Tests(unittest.TestCase):
    def test_cyclic_rotation_sample_test_01(self):
        a = [3, 8, 9, 7, 6]
        k = 3
        res = Lesson02.cyclic_rotation(a, k)
        self.assertEqual([9, 7, 6, 3, 8], res)

    def test_cyclic_rotation_sample_test_02(self):
        a = [0, 0, 0]
        k = 1
        res = Lesson02.cyclic_rotation(a, k)
        self.assertEqual([0, 0, 0], res)

    def test_cyclic_rotation_sample_test_03(self):
        a = [1, 2, 3, 4]
        k = 4
        res = Lesson02.cyclic_rotation(a, k)
        self.assertEqual([1, 2, 3, 4], res)

    def test_odd_occurrences_in_array_sample_test_01(self):
        a = [9, 3, 9, 3, 9, 7, 9]
        res = Lesson02.odd_occurrences_in_array(a)
        self.assertEqual(7, res)


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


if __name__ == '__main__':
    unittest.main()
