import unittest
import sys
sys.path.append('../')
from problems_vs_algorithms.problem_3 import rearrange_digits

class TestRearrangeDigits(unittest.TestCase):

    def _test_function(self, test_case):
        output = rearrange_digits(test_case[0])
        print(test_case[0], '=>', output)
        solution = test_case[1]
        self.assertEqual(sum(output), sum(solution))

    def test_problem_3_unsorted_array(self):
        print('\033[32m', "\nProblem 3: Test multiple unsorted arrays", '\033[0m')
        print("Odd Array: ")
        self._test_function([[1, 2, 3, 4, 5], [531, 42]])
        self._test_function([[9, 9, 9, 1, 8, 7, 6], [9971, 986]])
        self._test_function([[1, 8, 9, 5, 3, 2, 6], [9631, 852]])
        
        print("Even Array: ")
        self._test_function([[4, 6, 2, 7, 9, 8], [974, 862]])
        self._test_function([[9, 2, 5, 6, 0, 4], [952, 640]])

    def test_problem_3_same_values_array(self):
        print('\033[32m', "\nProblem 3: Test array with same values", '\033[0m')
        self._test_function([[1, 1, 1, 1, 1], [111, 11]])
        self._test_function([[3, 3, 3, 3], [33, 33]])

    def test_problem_3_same_no_values(self):
        print('\033[32m', "\nProblem 3: Test array with no values", '\033[0m')
        self._test_function([[], []])




if __name__ == '__main__':
    print("\n =========== PROBLEM 3 TESTS ==========")
    unittest.main()