class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Entry(object):
    def __init__(self, value, ref):
        self.value = value
        self.ref = ref

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        return new_node

    def delete(self, node):
        if node == self.head:
            self.head = node.next
            node = None
            return
        if node == self.tail:
            self.tail = node.prev
            node = None
            return
        node.next.prev = node.prev
        node.prev.next = node.next
        
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.current_capacity = 0
        self.cache = {}
        self.keys_list = LinkedList()


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        entry = self.cache.get(key)
        if entry is not None:
            if key != self.keys_list.tail.value:
                self.keys_list.delete(entry.ref)
                entry.ref = self.keys_list.append(key)
            return entry.value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        entry = self.get(key)
        if entry != -1:
            entry = self.cache.get(key)
            self.cache[key] = Entry(value, entry.ref)
            return
        
        new_node = self.keys_list.append(key)
        if self.current_capacity < self.capacity:
            self.cache[key] = Entry(value, new_node)
            self.current_capacity += 1
        else:
            lru = self.keys_list.head
            self.cache.pop(lru.value)
            self.keys_list.delete(lru)
            self.cache[key] = Entry(value, new_node)

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print('1 => ', our_cache.get(1))       # returns 1
print('2 => ', our_cache.get(2))      # returns 2
print('9 => ', our_cache.get(9))      # returns -1

our_cache.set(5, 5) 
our_cache.set(6, 6)

print('3 => ', our_cache.get(3))      # returns -1
