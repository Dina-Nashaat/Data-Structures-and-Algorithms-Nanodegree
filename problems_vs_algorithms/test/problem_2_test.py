import unittest
import sys
sys.path.append('../')
from problems_vs_algorithms.problem_2 import search_rotated

class TestSearchRotated(unittest.TestCase):
    def test_problem_2_element_is_found(self):
        ls = [4,5,6,7,0,1,2]
        print('\033[32m', "\nProblem 2: It should find present element in rotated array: [4,5,6,7,0,1,2]", '\033[0m')
        
        index = search_rotated(ls, 4)
        print("\n Index of 4 =>", index)
        self.assertEqual(index, 0)
        
        index = search_rotated(ls, 2)
        print("\n Index of 2 =>", index)
        self.assertEqual(index, 6)
        
        index = search_rotated(ls, 0)
        print("\n Index of 0 =>", index)
        self.assertEqual(index, 4)

    def test_problem_2_element_is_not_found(self):
        print('\033[32m', "\nProblem 2: It should not find missing element in rotated array: [4,5,6,7,0,1,2]", '\033[0m')
        ls = [4,5,6,7,0,1,2]
        
        index = search_rotated(ls, 3)
        print("\n Index of 3 =>", index)
        self.assertEqual(index, -1)

    def test_problem_2_element_is_found_in_two_elements_array(self):
        print('\033[32m', "\nProblem 2: It should find present element in array of length 2: [1, 3]", '\033[0m')
        ls = [1, 3]

        index = search_rotated(ls, 3)
        print("\n Index of 3 =>", index)
        self.assertEqual(index, 1)

        index = search_rotated(ls, 1)
        print("\n Index of 1 =>", index)
        self.assertEqual(index, 0)

    def test_problem_2_element_is_found_in_one_element_array(self):
        print('\033[32m', "\nProblem 2: It should find present element in array of length 1: [4]", '\033[0m')
        ls = [4]

        index = search_rotated(ls, 4)
        print("\n Index of 4 =>", index)
        self.assertEqual(index, 0)

    def test_problem_2_element_is_found_with_no_rotation(self):
        print('\033[32m', "\nProblem 2: It should find present element in array with no rotation", '\033[0m')
        ls = [0, 1, 2, 4, 5, 6, 7]

        index = search_rotated(ls, 0)
        print("\n Index of 0 =>", index)
        self.assertEqual(index, 0)

    def test_problem_2_element_is_not_found_in_empty_list(self):
        print('\033[32m', "\nProblem 2: It should not find element in empty array", '\033[0m')
        ls = []
        
        index = search_rotated(ls, 6)
        print("\n Index of 6 =>", index)
        self.assertEqual(index, -1)
    
    def test_problem_2_element_is_found_with_array_of_negative_numbers(self):
        print('\033[32m', "\nProblem 2: It should find element in rotated array with negative numbers: [4, 5, 6, 7, -5, 0, 1, 2]", '\033[0m')
        ls = [4, 5, 6, 7, -5, 0, 1, 2]

        index = search_rotated(ls, -5)
        print("\n Index of -5 =>", index)
        self.assertEqual(index, 4)
        
if __name__ == '__main__':
    print("\n =========== PROBLEM 2 TESTS ==========")
    unittest.main()