from feistel_functions import FeistelFunctions

def xor(bs1, bs2):
    list_bytes = [b1 ^ b2 for b1, b2 in zip(bs1, bs2)]
    return bytearray(list_bytes)

class Feistel:
    def __init__(self, decipher=False, function=FeistelFunctions.exp):
        self.function = function
        self.decipher = decipher
    
    def encipher(self, picture, iter, key):
        half = len(picture) // 2
        left = picture[:half]
        right = picture[half:]

        if not self.decipher:
            new_left = right
            new_right = xor(left, self.function(right, iter, key))
        else:
            new_left = xor(right, self.function(left, iter, key))
            new_right = left

        enciphered = new_left + new_right
        return enciphered