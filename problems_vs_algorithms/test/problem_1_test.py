import unittest
import random
import math
import sys
sys.path.append('../')
from problems_vs_algorithms.problem_1 import sqrt_recursive


class TestSqrt(unittest.TestCase):

    def test_problem_1_special_case(self):
        print("\nTesting Special Cases: ")

        zero = sqrt_recursive(0)
        self.assertEqual(zero, 0)
        print('\nSqrt(0) =>',  zero)

        one = sqrt_recursive(1)
        self.assertEqual(one, 1)
        print('\nSqrt(1) =>', one)

        self.assertRaises(ValueError, sqrt_recursive, -1)
        print('\nSqrt(-1) => should raise error')

    def test_problem_1_perfect_squares_root(self):
        print("\nTesting perfect squares: ")

        print('\nSqrt(2) =>', sqrt_recursive(2))
        self.assertEqual(sqrt_recursive(2), 1)
        self.assertEqual(sqrt_recursive(4), 2)
        self.assertEqual(sqrt_recursive(9), 3)
        self.assertEqual(sqrt_recursive(16), 4)
        self.assertEqual(sqrt_recursive(25), 5)
        self.assertEqual(sqrt_recursive(36), 6)
        print('\nSqrt(49) =>', sqrt_recursive(7))
        self.assertEqual(sqrt_recursive(49), 7)
        self.assertEqual(sqrt_recursive(64), 8)
        self.assertEqual(sqrt_recursive(81), 9)
        self.assertEqual(sqrt_recursive(100), 10)
        
    def test_problem_1_floor_root(self):
        print("\nTesting floor: ")

        print('\nSqrt(28) =>', sqrt_recursive(5))
        self.assertEqual(sqrt_recursive(28), 5)
        self.assertEqual(sqrt_recursive(455), 21)
        print('\nSqrt(77) =>', sqrt_recursive(8))
        self.assertEqual(sqrt_recursive(77), 8)
        self.assertEqual(sqrt_recursive(3), 1)
        self.assertEqual(sqrt_recursive(90), 9)
        r = random.randrange(0, 9999)
        self.assertEqual(sqrt_recursive(r), math.floor(math.sqrt(r)))

if __name__ == '__main__':
    print("\n =========== PROBLEM 1 TESTS ==========")
    unittest.main(verbosity=1)