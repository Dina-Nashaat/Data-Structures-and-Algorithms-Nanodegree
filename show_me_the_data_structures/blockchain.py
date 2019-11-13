import hashlib
import datetime

class Block:

    def __init__(self, index, timestamp, data, previous_hash, is_genesis=False):
      self.index = index
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.is_genesis = is_genesis

    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = f"{self.data}{self.timestamp}{self.previous_hash}".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.index = 1
        genesis_block = Block(
            self.index,
            datetime.datetime.utcnow(),
            'First Block',
            '0',
            True
        )
        self.map = dict()
        self.map[genesis_block.hash] = genesis_block
        self.tail = genesis_block
        
    def add_block(self, data):
        self.index += 1
        self.tail = Block(
            self.index,
            datetime.datetime.utcnow(),
            data,
            self.tail.hash
        )
        self.map[self.tail.hash] = self.tail
    
    def print_blockchain(self):
        block = self.tail
        while not block.is_genesis:
            self.__print_statement(block)
            block = self.map[block.previous_hash]
    
    def __print_statement(self, block):
        print(f'Block Index => {block.index}')
        print(f'timestamp => {block.timestamp}')
        print(f'data => {block.data}')
        print(f'hash => {block.hash}')
        print(f'previous hash => {block.previous_hash}')
        print('--------------------')


# Test 1
print("Test 1")
myBlockChain = BlockChain()
myBlockChain.add_block('New Data1')
myBlockChain.add_block('New Data2')
myBlockChain.add_block('New Data3')
myBlockChain.add_block('New Data4')
myBlockChain.add_block('New Data5')
myBlockChain.add_block('New Data6')
myBlockChain.add_block('New Data7')
myBlockChain.print_blockchain()

# Test 2
print("Test 2")
myBlockChain = BlockChain()
myBlockChain.print_blockchain()

# Test 3
print("Test 3")
myBlockChain = BlockChain()
myBlockChain.add_block(None)
myBlockChain.add_block(None)
myBlockChain.print_blockchain()

