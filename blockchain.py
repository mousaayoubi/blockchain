from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []
        self.all_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transaction = []
        previous_hash = '0'
        genesis_block = Block(transaction, previous_hash)
        genesis_block.generate_hash()
        self.chain.append(genesis_block)

    def add_block(self, transaction):
        previous_hash = self.chain[len(self.chain)-1].hash
        new_block = Block(transaction, previous_hash)
        new_block.generate_hash()
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)

    def validate_blocks(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if current.hash != current.generate_hash():
                print("Invalid blockchain. Values have been modified.")
                return False

            if current.previous_hash != previous.generate_hash():
                print("Invalid blockchain. Values have been modified.")
                return False
        print("This blockchain is valid.")
        return True

    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_contents()

    def proof_of_work(self, block, difficulty = 2):
        proof = block.generate_hash()

        while proof[:difficulty] != '0' * difficulty:
            block.nonce += 1
            proof = block.generate_hash()

        block.nonce = 0
        return proof
