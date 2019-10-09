import unittest
from Solutions import Lesson03


class PermMissingTests(unittest.TestCase):
    def test_perm_missing_elem_example_test_01(self):
        a = [2, 3, 1, 5]
        res = Lesson03.perm_missing_elem(a)
        self.assertEqual(4, res)
