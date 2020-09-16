from blockchain import Blockchain

transaction1 = {
        'Sender': 'Mousa',
        'Receiver': 'Bob',
        'Amount': '100'
        }

transaction2 = {
        'Sender': 'John',
        'Receiver': 'Jane',
        'Amount': '200'
        }

transaction3 = {
        'Sender': 'Tim',
        'Receiver': 'Ann',
        'Amount': '250'
        }

block1 = Blockchain()
block1.add_block(transaction1)
block1.add_block(transaction2)
block1.add_block(transaction3)
block1.print_blocks()
block1.validate_blocks()
