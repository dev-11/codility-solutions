import unittest
from Solutions import Lesson02


class CyclicRotationTests(unittest.TestCase):
    def test_cyclic_rotation_example_test_01(self):
        a = [3, 8, 9, 7, 6]
        k = 3
        res = Lesson02.cyclic_rotation(a, k)
        self.assertEqual([9, 7, 6, 3, 8], res)

    def test_cyclic_rotation_example_test_02(self):
        a = [0, 0, 0]
        k = 1
        res = Lesson02.cyclic_rotation(a, k)
        self.assertEqual([0, 0, 0], res)

    def test_cyclic_rotation_example_test_03(self):
        a = [1, 2, 3, 4]
        k = 4
        res = Lesson02.cyclic_rotation(a, k)
        self.assertEqual([1, 2, 3, 4], res)
