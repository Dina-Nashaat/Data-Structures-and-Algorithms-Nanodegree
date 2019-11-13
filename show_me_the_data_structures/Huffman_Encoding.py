import sys
from queue import PriorityQueue

class HuffmanNode(object):
    def __init__(self, count = 0, char = None, right = None, left = None):
        self.char = char
        self.count = count
        self.right = right
        self.left = left
    
    def __lt__(self, node):
        return self.char and node.char and self.char < node.char

    def __repr__(self):
        return f"{self.char} => {self.count}"

class Huffman(object):

    def encode(self, data):
        chars = dict()

        for c in data:
            if chars.get(c):
                huff_node = chars[c]
                huff_node.count += 1
            else:
                chars[c] = HuffmanNode(1, c)
        chars['EOF'] = HuffmanNode(1, 'EOF')

        p_queue = self.__build_priority_queue(chars)
        root = self.__build_huffman_tree(p_queue)
        encoding_map = self.__traverse_huffman_tree(root)
        encoded_data = ''

        for ch in data:
            encoded_data = encoded_data + encoding_map[ch] 

        return encoded_data, root
        
    def decode(self, data, root):
        decoded = ''
        node = root
        for b in data:
            if b == '1':
                if node.right.char is None:
                    node = node.right
                else:
                    decoded += node.right.char
                    node = root
            else:
                if node.left.char is None:
                    node = node.left
                else:
                    decoded += node.left.char
                    node = root
                
        return decoded

    def __build_priority_queue(self, chars_map): 
        q = PriorityQueue()
        for key in chars_map:
            node = chars_map[key]
            q.put((node.count, node))
        return q

    def __build_huffman_tree(self, priority_queue):
        while priority_queue.qsize() > 1:
            (leftCount, leftNode) = priority_queue.get()
            (rightCount, rightNode) = priority_queue.get() if not priority_queue.empty() else (0, HuffmanNode())
            parent = HuffmanNode(leftCount + rightCount, left = leftNode, right = rightNode)
            priority_queue.put((parent.count, parent))
        return priority_queue.get()[1]

    def __traverse_huffman_tree(self, root):
        encoding_map = dict()
        self.__traverse_huffman_tree__(root, '', encoding_map)
        return encoding_map

    def __traverse_huffman_tree__(self, node, code, encoding_map):
        if node.left is None:
            encoding_map[node.char] = code
            return
        if node.right is None:
            encoding_map[node.char] = code
            return
        self.__traverse_huffman_tree__(node.left, code + '0', encoding_map)
        self.__traverse_huffman_tree__(node.right, code + '1', encoding_map)

if __name__ == "__main__":
    huffman = Huffman()

    test_case_1 = "The bird is the word"
    test_case_2 = "aaaaaaaaaaaaaaaaaaaa"
    test_case_3 = ""

    encoded_data, tree = huffman.encode(test_case_1)
    print("TEST 1: ")
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman.decode(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    encoded_data, tree = huffman.encode(test_case_2)
    print("TEST 2: ")
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman.decode(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    encoded_data, tree = huffman.encode(test_case_3)
    print("TEST 3: ")
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman.decode(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))