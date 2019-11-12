# LRU Cache
## Data Structures used:
- Doubly Linked List
- Dictionary  
 For an LRU cache, the least recent item gets replaced with the newest item when the cache reaches its capacity. To achieve this purpose, a doubly linked list is used as a queue, every time an item is set, the old key (head) is removed and the new key is enqueued into the `keys_list` and if the enqueued item already exists, it gets deleted from the doubly linked list. The same algorithm goes when accessing an item, however, we don't remove the least recently used, but we update the tail of the queue.
 
To delete in constant time, a doubly linked list was used. Given a node, we update its previous and next references in constant time.

The cache itself is a hashmap to allow for constant retrieval time. The cache entry key is the user specified key, and cache value is an Entry Class that contains two information; the value at the key, and a reference to the node in the doubly linked list (to allow constant delete time)

Note: LRU has two implementation, the first implementation uses an implemented Doubly Linked List, and the second uses OrderedMap which uses a doubly linked list under the hood and provides constant delete time.


## Complexity:
Get: O(1)
Set: O(1)


# File Recursion

## Complexity:
Let `d` be the total number of directories in one path  
Complexity is: `O(d)`

# Huffman Encoding:
## Data Structure used:
- Priority Queue (Min Heap Tree)
- Dictionary

A binary tree is used to create the huffman tree, and the dictionary contains a mapping between the letter and its code.

## Complexity:
let 
`n` is the length of string  
`m` length of unique characters
`k` length of huffman tree nodes
### Encoding:
- Count frequencies: `O(n)`
- Building a priority queue: `O(m * log(m))` (priority put is log(n))
- Build Huffman Tree: `O(k * log(k))`
- Traverse Huffman Tree: `O(k)`  

Overall: `O(n) + O(m * log(m)) + O(k * log(k)) + O(k) = O(k * log(k))`  
O(n) since it's the least complexity is ignored  
O(m log(m)) is ignored, since m is less than k (m is number of leaf nodes, k is number of all nodes)  
therefore the overall complexity is `O(k * log(k))`

### Decoding:
`n` is the length of string  
`k` is the number of k nodes  
Overall: O(n * log(k))

# BlockChain
## Data Structure used:
- Dictionary
- LinkedList  

A blockchain is similar to a linked list, it consists of nodes and each node has a reference through hash
to the previous node. To provide constant lookup / put time, we used a dictionary that stores as a key the blockchain hash and its value is the block reference to be easily accessible

### Adding a block: `O(1)`
### Printing a block: `O(n)`

# Active Directory
## Data Structure used:
- Arrays

## Complexity:
O(u + g)  
where u is number of users and g is the number of groups in the group tree

# Union Intersection:
- LinkedList
- Dictionary  

An additional dictionary is used in union and intersection to be able to retrieve information on previously
visited nodes. In union we need the info so as not to duplicate nodes, and in intersection we need to keep track which node appeared at least once in both lists

## Union:
Complexity: `O(n + m)` where n is the number of nodes in List 1 and m is the number of nodes in List 2

## Intersection:
Complexity: `O(n + m`