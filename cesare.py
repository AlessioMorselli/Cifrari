import random

def rotate(l, n):
    return l[n:] + l[:n]

class Cesare:
    def __init__(self, offset=random.randint(1, 25)):
        self.offset = offset
    
    def encipher(self, alfabeto):
        return rotate(alfabeto, self.offset)
    