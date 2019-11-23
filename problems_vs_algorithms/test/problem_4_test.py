import unittest
import sys
sys.path.append('../')
from problems_vs_algorithms.problem_4 import sort_012_method_1

class TestDutchFlag(unittest.TestCase):
    def test_problem_4_unsorted_array(self):
        print('\033[32m', "\nProblem 4: Test multiple unsorted arrays", '\033[0m')
        arr1 = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
        expected1 = sorted(arr1)
        actual1 = sort_012_method_1(arr1)
        print([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1], '=>', actual1)
    
        arr2 = [1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 0]
        expected2 = sorted(arr2)
        actual2 = sort_012_method_1(arr2)
        print([1, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 0], '=>', actual2)

        self.assertEqual(expected1, actual1)
        self.assertEqual(expected2, actual2)

    def test_problem_4_empty_array(self):
        print('\033[32m', "\nProblem 4: Test Empty array", '\033[0m')
        arr = []
        expected = sorted(arr)
        actual = sort_012_method_1(arr)
        print([], '=>', actual)
        self.assertEqual(expected, actual)

    def test_problem_4_sorted_array(self):
        print('\033[32m', "\nProblem 4: Test Sorted Array", '\033[0m')
        arr = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
        expected = sorted(arr)
        actual = sort_012_method_1(arr)
        print([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2], '=>', actual)
        self.assertEqual(expected, actual)

    def test_problem_4_short_array(self):
        print('\033[32m', "\nProblem 4: Test short array", '\033[0m')
        arr = [2, 0, 1]
        expected = sorted(arr)
        actual = sort_012_method_1(arr)
        print([2, 0, 1], '=>', actual)
        self.assertEqual(expected, actual)

    
if __name__ == '__main__':
    print("\n =========== PROBLEM 6 TESTS ==========")
    unittest.main()