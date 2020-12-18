import datetime
import hashlib

class Block:
        blockNum = 0
        data = None
        next = None
        hash = None
        nonce = 0
        previous_hash = 0x0
        timestamp = datetime.datetime.now()

        def __init__(self, data):
            self.data = data

        def hash(self):
            h = hashlib.sha256()
            h.update(
                str(self.nonce).encode('utf-8') +
                str(self.data).encode('utf-8') +
                str(self.previous_hash).encode('utf-8') +
                str(self.timestamp).encode('utf-8') +
                str(self.blockNum).encode('utf-8')
            )
            return h.hexdigest()
        def __str__(self):
            return f"Block hash is: {self.hash()} + \nBlock Number: {self.blockNum}"

class Blockchain:
    diff = 20
    maxNonce = 2**32
    target = 2**(256-diff)

    #genesis first block
    block = Block("Genesis")
    head = block

    def add(self, block):
        block.previous_hash = self.block.hash()
        block.blockNum = self.block.blockNum + 1
        self.block.next = block
        self.block = self.block.next

#mining
    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1
bc = Blockchain()

for num in range(5):
    bc.mine(Block("Block "+ str(num + 1)))

while bc.head != None:
    print(bc.head)
    bc.head = bc.head.next
