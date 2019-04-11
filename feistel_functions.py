class FeistelFunctions:

    @staticmethod
    def identity(bs, i, key):
        return bs
    
    @staticmethod
    def exp(bs, i, key):
        tmp = [pow(2 * i * key, b) % 256 for b in bs]
        return bytearray(tmp)