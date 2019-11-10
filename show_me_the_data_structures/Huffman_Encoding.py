import sys

class HuffmanNode(object):
    def __init__(self, count = 0, char = None, left = None, right = None):
        self.char = char
        self.count = count
        self.left = left
        self.right = right
    def __repr__(self):
        return str(self.char) + ' => ' + str(self.count)

class Huffman(object):

    def encode(self, data):
        chars = dict()

        # Count frequencies
        for c in data:
            if chars.get(c):
                huff_node = chars[c]
                huff_node.count += 1
            else:
                chars[c] = HuffmanNode(1, c)
        chars['EOF'] = HuffmanNode(1, 'EOF')

        # Build a sorted list
        sorted_list = self.__build_sorted_list(chars)

        # Build Huffman Tree
        root = self.__build_huffman_tree(sorted_list)

        # Traverse tree
        encoding_map = dict()
        self.__traverse_huffman_tree(root, '', encoding_map)

        # Construct encoded bits
        encoded_data = ''
        for ch in data:
            encoded_data = encoded_data + encoding_map[ch] 

        return encoded_data, root

    def __build_sorted_list(self, chars):
        huff_nodes = []
        for char in chars:
            huff_nodes.append(chars[char])

        return sorted(huff_nodes, key=lambda huff_node: huff_node.count)
        
    def __build_huffman_tree(self, ls):
        while len(ls) > 1:
            left = ls.pop(0)
            right = ls.pop(0) if ls else HuffmanNode()
            parent = HuffmanNode(left.count + right.count)
            parent.left = left
            parent.right = right
            ls = self.__insert_in_sorted(ls, parent)

        return ls[0]         

    def __insert_in_sorted(self, ls, element):
        index = len(ls)
        for i, huff_node in enumerate(ls):
            if huff_node.count > element.count:
                index = i
                break
        ls = ls[:index] + [element] + ls[index:]
        return ls

    def __traverse_huffman_tree(self, node, code, encoding_map):
        if node.left is None:
            encoding_map[node.char] = code
            return
        if node.right is None:
            encoding_map[node.char] = code
            return
        self.__traverse_huffman_tree(node.left, code + '0', encoding_map)
        self.__traverse_huffman_tree(node.right, code + '1', encoding_map)
        
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


if __name__ == "__main__":

    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    huffman = Huffman()
    encoded_data, tree = huffman.encode(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman.decode(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
