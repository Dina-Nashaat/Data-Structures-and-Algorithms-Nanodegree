class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        out_string += 'None'
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    visited = {}
    unionList = LinkedList()
    curr_node = llist_1.head
    while curr_node is not None:
        if not visited.get(curr_node.value):
            visited[curr_node.value] = True
            unionList.append(curr_node.value)
        curr_node = curr_node.next
    
    curr_node = llist_2.head
    while curr_node is not None:
        if not visited.get(curr_node.value):
            visited[curr_node.value] = True
            unionList.append(curr_node.value)
        curr_node = curr_node.next
    return unionList

def intersection(llist_1, llist_2):
    visited = {}
    intersectionList = LinkedList()
    
    curr_node = llist_1.head
    while curr_node is not None:
        if visited.get(curr_node.value) is None:
            visited[curr_node.value] = 0
        curr_node = curr_node.next
    
    curr_node = llist_2.head
    while curr_node is not None:
        if visited.get(curr_node.value) == 0:
            visited[curr_node.value] += 1
            intersectionList.append(curr_node.value)
        curr_node = curr_node.next
    return intersectionList


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print('Union: ')
print (union(linked_list_1,linked_list_2)) #[3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11]
print('Intersection')
print (intersection(linked_list_1,linked_list_2)) #[4, 6, 21]

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)
print('\n')
print('Union: ')
print (union(linked_list_3,linked_list_4)) #[3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21]
print('Intersection')
print (intersection(linked_list_3,linked_list_4)) #[]
