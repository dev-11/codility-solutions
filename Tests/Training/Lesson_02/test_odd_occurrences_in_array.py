import unittest
from Solutions import Lesson02


class Lesson02Tests(unittest.TestCase):
    def test_odd_occurrences_in_array_example_test_01(self):
        a = [9, 3, 9, 3, 9, 7, 9]
        res = Lesson02.odd_occurrences_in_array(a)
        self.assertEqual(7, res)
