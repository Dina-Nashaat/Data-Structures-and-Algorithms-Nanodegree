# Problem 1


# Problem 2


# Problem 6

To find the maximum and minimum, we could go with several approaches. 
1. Sort the array and extract the first and last element (Expensive) O(n*log(n))
2. Traverse the list twice to get the maximum and minimum independantly
    - Number of Comparisons: 2 comparisons per iteration `2 * (n - 1) = 2n - 2`
    - Time Complexity: O(n), Space Complexity: O(n)
3. Traverse once and compare each 2 pair of adjacent elements together and get the `localMin` and  
`localMax` then compare them with the current `globalMin` and `globalMax` (Divide and Conquer)
    - Number of Comparisons: 3 comparisons per 2 elements `3 * (n//2)`
    - Time Complexity: o(n), space Complexity: O(n)
