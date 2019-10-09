import unittest
from Solutions import Lesson05


class PassingCarsTests(unittest.TestCase):
    def test_passing_cars_example_test_01(self):
        a = [0, 1, 0, 1, 1]
        res = Lesson05.passing_cars(a)
        self.assertEqual(5, res)

