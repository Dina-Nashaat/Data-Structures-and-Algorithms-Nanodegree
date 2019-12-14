def inverseWeightedArray(array):
    # Time Complexity : O(n + m)
    depth = getDepth(array)
    max_sum = getSum(array, depth)
    return max_sum

# Complexity O(n) where n is the number of depths in one array
def getDepth(array):
    max_depth = 0
    for el in array:
       if isinstance(el, list):
           depth = getDepth(el)
           max_depth = max(depth, max_depth)
    return max_depth + 1

# Complexity O(m) where m is the number of integers in array
def getSum(array, depth):
    combined = 0
    for el in array:
        if isinstance(el, int):
            combined += el * depth
        elif isinstance(el, list):
            combined += getSum(el, depth - 1)
    return combined

print(inverseWeightedArray([[1,1],2,[1,1]]), 8)
print(inverseWeightedArray([1,[4,[6]]]), 6 + 8 + 3)
# 6 * 1 = 6
# 4 * 2 = 8
# 1 * 3 = 3
# 6 + 8 + 3 = 17
print(inverseWeightedArray([[[1],1],2,[1,1]]), 13)
# 1 * 1 = 1
# 1 * 2 = 2
# 2 * 3 = 6
# 1 * 2 + 1 * 2 = 4
print(inverseWeightedArray([[1,1],2,[1,[1]]]), 13)
# 1 * 2 + 1 * 2 =  4
# 2 * 3 = 6
# 1 * 2 + 1 * 1 = 3
print(inverseWeightedArray([]), 0)
print(inverseWeightedArray([[[[]]], 1]), 4)
# 1 * 4 = 4
print(inverseWeightedArray([[[[1]]], 1]), 5)
# 1 * 1 = 1
# 1 * 4 = 4