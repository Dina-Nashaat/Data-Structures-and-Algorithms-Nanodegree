from collections import OrderedDict 

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.current_capacity = 0
        self.cache = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        value = self.cache.get(key) or -1
        if value > -1 :
            self.cache.pop(key)
            self.cache[key] = value
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.capacity == 0:
            return
        entry = self.get(key)
        if entry != -1:
            self.cache[key] = value
            return

        if self.current_capacity < self.capacity:
            self.current_capacity += 1
        else:
            self.cache.popitem(last=False) #FIFO
        self.cache[key] = value

    def print_cache(self):
        print(self.cache)

# TEST 1
our_cache = LRU_Cache(3)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print("TEST 1: ")
print('1 => ', our_cache.get(1))      # returns -1 => [4, 2, 3]
print('2 => ', our_cache.get(2))      # returns 2 => [3, 4, 2]
print('9 => ', our_cache.get(9))      # returns -1 => [3, 4, 2]
our_cache.set(5, 5) # => [4, 2, 5]
our_cache.set(6, 6) # => [2, 5, 6]
print('3 => ', our_cache.get(3))      # returns -1

# TEST 2
print("TEST 2: ")
our_cache = LRU_Cache(3)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print('4 => ', our_cache.get(4))      # returns 4, [2, 3, 4]
print('3 => ', our_cache.get(3))      # returns 3, [2, 4, 3]
print('1 => ', our_cache.get(1))      # returns -1 [2, 4, 3]
our_cache.set(5, 5) # [4, 3, 5]
our_cache.set(6, 6) # [3, 5, 6]
print('3 => ', our_cache.get(3))      # returns 3

# TEST 3
print("TEST 3: ")
our_cache = LRU_Cache(0)
our_cache.set(1, 1)
print('1 => ', our_cache.get(1))      # returns -1
