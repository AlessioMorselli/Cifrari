class FeistelFunctions:

    @staticmethod
    def identity(bs, key):
        return bs
    
    @staticmethod
    def exp3(bs, key):
        tmp = [pow(3 * key, b) % 256 for b in bs]
        return bytearray(tmp)
    
    @staticmethod
    def exp5(bs, key):
        tmp = [pow(5 * key, b) % 256 for b in bs]
        return bytearray(tmp)
    
    @staticmethod
    def exp7(bs, key):
        tmp = [pow(7 * key, b) % 256 for b in bs]
        return bytearray(tmp)
    
    @staticmethod
    def exp11(bs, key):
        tmp = [pow(11 * key, b) % 256 for b in bs]
        return bytearray(tmp)