import math
import random


class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(
                num, prime-1)
            raise ValueError(error)

        self.num = num
        self.prime = prime

        def __repr__(self):
            return 'FieldElement_{} ({})'.format(
                self.prime, self.num)

        def __eq__(self, other):
            if other is None:
                return False
            return self.num == other.num and self,prime == other.prime
            pass

def Merkel_tree():
    total = int(input("Enter num of nodes: "))
    max_depth = math.ceil(math.log(total, 2))
    merkle_tree = []
    for depth in range(max_depth + 1):
        num_items = math.ceil(total / 2**(max_depth - depth))
        hash = random.getrandbits(128)
        level_hashes = [hash] * num_items
        merkle_tree.append(level_hashes)
    for level in merkle_tree:
        print(level)

Merkel_tree()