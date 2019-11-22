import unittest
import sys
sys.path.append('../')
from problems_vs_algorithms.problem_6 import get_min_max

class TestSearchRotated(unittest.TestCase):
    def test_problem_6_returns_max_min_within_array_with_even_size(self):
        l = [i for i in range(1, 11)]
        print('\033[32m', "\nProblem 6: return max and min from unsorted array of even size: ", '\033[0m')
        
        min_max = get_min_max(l)
        print(l, "=>", min_max)
        self.assertEqual(min_max, (1, 10))

    def test_problem_6_returns_max_min_within_array_with_odd_size(self):
        l = [i for i in range(1, 12)]
        print('\033[32m', "\nProblem 6: return max and min from unsorted array of odd size: ", '\033[0m')

        min_max = get_min_max(l)
        print(l, "=>", min_max)
        self.assertEqual(min_max, (1, 11))
    
    def test_problem_6_returns_nothing_with_empty_list(self):
        l = []
        print('\033[32m', "\nProblem 6: return None if list is empty: ", '\033[0m')

        min_max = get_min_max(l)
        print(l, "=>", min_max)
        self.assertEqual(min_max, None)

    def test_problem_6_returns_same_element_with_list_of_one_element(self):
        l = [1]
        print('\033[32m', "\nProblem 6: return same number if list has one element: ", '\033[0m')
        
        min_max = get_min_max(l)
        print(l, "=>", min_max)
        self.assertEqual(min_max, (1, 1))

    def test_problem_6_returns_max_min_within_array_with_elements_of_same_value(self):
        l = [6] * 9
        print('\033[32m', "\nProblem 6: return same number if list has elements of same value: ", '\033[0m')
        
        min_max = get_min_max(l)
        print(l, "=>", min_max)
        self.assertEqual(get_min_max(l), (6, 6))
    
if __name__ == '__main__':
    print("\n =========== PROBLEM 6 TESTS ==========")
    unittest.main()