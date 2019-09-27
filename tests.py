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


class Lesson05Tests(unittest.TestCase):
    def test_passing_cars_sample_test_01(self):
        a = [0, 1, 0, 1, 1]
        res = Lesson05.passing_cars(a)
        self.assertEqual(5, res)


# class Lesson06Tests(unittest.TestCase):


class Lesson07Tests(unittest.TestCase):
    def test_brackets_sample_test_01(self):
        s = "{[()()]}"
        res = Lesson07.brackets(s)
        self.assertEqual(res, 1)

    def test_brackets_sample_test_02(self):
        s = "([)()]"
        res = Lesson07.brackets(s)
        self.assertEqual(res, 0)

    def test_nesting_sample_test_01(self):
        s = "(()(())())"
        res = Lesson07.nesting(s)
        self.assertEqual(res, 1)

    def test_nesting_sample_test_02(self):
        s = "())"
        res = Lesson07.nesting(s)
        self.assertEqual(res, 0)



class Lesson08Tests(unittest.TestCase):
    def test_dominator_sample_test_01(self):
        a = [3, 4, 3, 2, 3, -1, 3, 3]
        res = Lesson08.dominator(a)
        self.assertIn(res, [0, 2, 4, 6, 7])


if __name__ == '__main__':
    unittest.main()
