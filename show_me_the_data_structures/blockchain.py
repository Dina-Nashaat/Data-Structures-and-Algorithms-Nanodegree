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
    
    def print_block(self):
        block = self.tail
        while not block.is_genesis:
            print(f'[{block.index}] => {block.data}')
            block = self.map[block.previous_hash]
        print(f'[{block.index}] => {block.data}')


myBlockChain = BlockChain()
myBlockChain.add_block('New Data1')
myBlockChain.add_block('New Data2')
myBlockChain.add_block('New Data3')
myBlockChain.add_block('New Data4')
myBlockChain.add_block('New Data5')
myBlockChain.add_block('New Data6')
myBlockChain.add_block('New Data7')

myBlockChain.print_block()