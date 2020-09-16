from datetime import datetime
from hashlib import sha256

class Block:
    def __init__(self, transaction, previous_hash, nonce = 0):
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.timestamp = datetime.now()
        self.nonce = nonce
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_header = str(self.transaction) + str(self.previous_hash) + str(self.timestamp) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()

    def print_contents(self):
        print("Timestamp: ", self.timestamp)
        print("Transaction: ", self.transaction)
        print("Current Hash: ", self.hash)
        print("Previous Hash: ", self.previous_hash)
