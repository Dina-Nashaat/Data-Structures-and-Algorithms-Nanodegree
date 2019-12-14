# k starts with 1
def fastSelect(ints, k):
    n = len(ints)
    if n == 0:
        return None

    if n == 1:
        return ints[0]

    groups_of_five = []
    for i in range(0, n, 5):
        groups_of_five.append(ints[i:i+5])

    medians = []
    for group in groups_of_five:
        sorted_group = sorted(group)
        mid = len(group) // 2
        medians.append(sorted_group[mid])
    
    p = fastSelect(medians, n//10)

    # [[x < p], [x = P], [x > p]]
    partitions = [[], [], []]
    for i in ints:
        if i < p:
            partitions[0].append(i)
        elif i == p:
            partitions[1].append(i)
        else:
            partitions[2].append(i)

    if k <= len(partitions[0]):
        return fastSelect(partitions[0], k)
    if k > (len(partitions[0]) + len(partitions[1])):
        return fastSelect(partitions[2], k - len(partitions[0]) - len(partitions[1]))
    else:
        return p


import random
l = [i for i in range(1, 500)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ( 250 == fastSelect(l, 250)) else "Fail")
def color_print(array, idx = [] , color = '\033[32m'):
    i = 0
    print("[", end='')
    while i < len(array):
        if i in idx:
            print(color, array[i],'\033[0m', end=', ', sep='')
        else:
            print(array[i], end = ', ')
        i += 1
    print(']')
