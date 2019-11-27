# Problem 1
To find the square root:
Use an approach similar to binary search, where we find the root either at a point greater than or less than the mid point.
- Time Complexity: O(log(n)) since we only traverse half the input every time
- Space Complexity: O(log(n)) due to the recursive function memory stack

# Problem 2
To find an element in a sorted list, we also use a similar approach to binary search, however we tweak the conditions. The function is recursive and only explores half the input every time it is called. 

- Time Complexity: O(log(n)) since we only traverse half the input every time
- Space Complexity: O(log(n)) due to the recursive function memory stack

# Problem 3
To find the maximum sum, we would solve on the assumption that the two maximum numbers formed by concatinating the odd indices to form the first number and concatinating the even indices to form the second. To achieve this, we need to sort the array from largest to smallest. 
 
We have used merge sort which gurantees: 
- Time Complexity: O(log(n))
- Space Complexity:  O(n)


# Problem 4
Dutch National Flag can be solved in various methods, but both involve the use of Partioning Algorithm

## Method 1:
In one pass, we have three pointers and a pivot. The pivot's value is one, to indicate the middle partition. The start pointer keeps track of the zeros partition, the mid pointer acts as an incrementor and keeps track of ones partition and end pointer gets decremented if the mid element is higher than the pivot (aka 2 > 1)
For example, after one pass the array indices should indicate the following:
consider a = [s .. e]
a[s -> z - 1] => Zeros Partition
a[z -> t - 1] => Ones Partition
a[t -> e] => Twos Partition

where s = start index,  e = end index, z = zero pointer, t = twos pointer

- Time Complexity: O(n)
- Space Complexity: O(1) where no extra space is used due to in place array swaps

## Method 2:
In two passes, first partition the array around pivot 1, where all 2s will be placed at the end and 0s and 1s will be scrambled at the left. Then partition the first half of the array around pivot 0.5, which will sort 0s and 1s in place

- Time Complexity: O(n)
- Space Complexity: O(1)

# Problem 5

Trie Insert:
- Time Complexity: O(n)
- Space Complexity: O(n)

Trie find:
- Time Complexity: O(n)
- Space Complexity: O(1)


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

# Problem 7:
Trie Insert:
- Time Complexity: O(n)
- Space Complexity: O(n)

Trie find:
- Time Complexity: O(n)
- Space Complexity: O(1)
