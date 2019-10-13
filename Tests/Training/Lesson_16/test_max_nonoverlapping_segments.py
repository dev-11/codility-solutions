import unittest
from Solutions import Lesson16

class MaxNonoverlappingSegmentsTest(unittest.TestCase):
    def test_max_nonoverlapping_segments_example_test01(self):
        a = [1, 3, 7, 9, 9]
        b = [5, 6, 8, 9, 10]
        res = Lesson16.max_nonoverlapping_segments(a, b)
        self.assertEqual(3, res)
 
