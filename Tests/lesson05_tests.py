import unittest
from Solutions import Lesson05


class Lesson05Tests(unittest.TestCase):
    def test_passing_cars_sample_test_01(self):
        a = [0, 1, 0, 1, 1]
        res = Lesson05.passing_cars(a)
        self.assertEqual(5, res)
