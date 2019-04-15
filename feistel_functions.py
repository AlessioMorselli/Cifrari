from des import expansion, xor, subtable, substitution, permutation
from des import divide_six_bits, concat_substitution_result

class FeistelFunctions:

    # @staticmethod
    # def identity(bs, key):
    #     return bs
    
    @staticmethod
    def exp3(bs, key):
        tmp = [pow(3 * key, b) % 256 for b in bs]
        return bytes(tmp)
    
    @staticmethod
    def exp5(bs, key):
        tmp = [pow(5 * key, b) % 256 for b in bs]
        return bytes(tmp)
    
    @staticmethod
    def exp7(bs, key):
        tmp = [pow(7 * key, b) % 256 for b in bs]
        return bytes(tmp)
    
    @staticmethod
    def exp11(bs, key):
        tmp = [pow(11 * key, b) % 256 for b in bs]
        return bytes(tmp)
    
    @staticmethod
    def des(pict, key):
        result = b''
        for i in range(len(pict) // 4):
            block = pict[i*4:(i+1)*4]
            exp_block = expansion(block)
            xor_block = xor(exp_block, key)
            six_bits = divide_six_bits(xor_block)
            subs = []
            for j in range(8):
                table = subtable(j + 1)
                subs.append(substitution(six_bits[j], table))
            sub = concat_substitution_result(subs)
            perm = permutation(sub)
            result += perm

        return result