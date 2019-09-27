import unittest
from Solutions.Lesson_01 import binary_gap


class Lesson01Tests(unittest.TestCase):
    def test_binary_gap_positive_test_01(self):
        n = 1041
        gap = binary_gap.solution(n)
        self.assertEqual(gap, 5)

    def test_binary_gap_positive_test_02(self):
        n = 32
        gap = binary_gap.solution(n)
        self.assertEqual(gap, 0)


if __name__ == '__main__':
    unittest.main()
