import unittest
import Solutions.Lesson_01 as Lesson01
import Solutions.Lesson_02 as Lesson02


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


if __name__ == '__main__':
    unittest.main()
