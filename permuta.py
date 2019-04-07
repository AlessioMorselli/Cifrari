import random

class Permuta:
    def __init__(self, alfabeto="abcdefghijklmnopqrstuvwxyz", shuffle=True):
        self.alfabeto = list(alfabeto)
        if shuffle:
            random.shuffle(self.alfabeto)
        self.alfabeto = ''.join(self.alfabeto)

    def encipher(self, alfabeto):
        return self.alfabeto