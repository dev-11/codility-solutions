import unittest
from Solutions import Lesson08


class EquiLeaderTests(unittest.TestCase):
    def test_equi_leader_example_test_01(self):
        a = [4, 3, 4, 4, 4, 2]
        res = Lesson08.equi_leader(a)
        self.assertEqual(2, res)

    def test_equi_leader_test_01(self):
        a = [1, 2]
        res = Lesson08.equi_leader(a)
        self.assertEqual(0, res)

    def test_equi_leader_test_02(self):
        a = [5]
        res = Lesson08.equi_leader(a)
        self.assertEqual(0, res)

    def test_equi_leader_test_03(self):
        a = [0, 0]
        res = Lesson08.equi_leader(a)
        self.assertEqual(1, res)
