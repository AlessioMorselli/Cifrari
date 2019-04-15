from bitarray import bitarray

def create_keys(key):
    keys = []
    key_56 = permuted_choice_1(key)
    for i in range(16):
        rotated_key = rotate_key(key_56, i)
        keys.append(permuted_choice_2(rotated_key))

def subtable(i):
    list_x = [  "0000", "0001", "0010", "0011",
                "0100", "0101", "0110", "0111",
                "1000", "1001", "1010", "1011",
                "1100", "1101", "1110", "1111"]
    list_y = ["00", "01", "10", "11"]

    table = {}
    with open("sub/sub" + str(i), "r") as f:
        for y in list_y:
            for x in list_x:
                n = int(f.readline())
                table[y[0] + x + y[1]] = n

    return table


def expansion(bs_32):
    # bs_32 è un gruppo di 32 bit (in formato bytes)
    # La funzione 'expansion' trasforma bs_32 in bs_48 secondo una tabella fissa
    exp = [ 32,  1,  2,  3,  4,  5,
             4,  5,  6,  7,  8,  9,
             8,  9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17,
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32,  1 ]
    # exp[i] = j => il bit i di bits_32 diventa il bit j di bits_48

    bits_32 = bitarray()
    bits_48 = bitarray([0 for i in range(48)])

    bits_32.frombytes(bs_32)
    
    for i in range(48):
        bits_48[i] = bits_32[exp[i] - 1]

    return bits_48.tobytes()

def permuted_choice_1(key):
    perm_1 = [  57, 49, 41, 33, 25, 17,  9,
                 1, 58, 50, 42, 34, 26, 18,
                10,  2, 59, 51, 43, 35, 27,
                19, 11,  3, 60, 52, 44, 36,
                63, 55, 47, 39, 31, 23, 15,
                 7, 62, 54, 46, 38, 30, 22,
                14,  6, 61, 53, 45, 37, 29,
                21, 13,  5, 28, 20, 12,  4 ]
    
    key_64 = bitarray()
    key_64.frombytes(key)

    key_56 = bitarray([0 for i in range(56)])

    for i in range(56):
        key_56[i] = key_64[perm_1[i] - 1]
    
    return key_56.tobytes()

def rotate_key(key, i):
    key_56 = bitarray()
    key_56.frombytes(key)

    return (key_56[i:] + key_56[:i]).tobytes()

def permuted_choice_2(key):
    perm_2 = [  14, 17, 11, 24,  1,  5,
                 3, 28, 15,  6, 21, 10,
                23, 19, 12,  4, 26,  8,
                16,  7, 27, 20, 13,  2,
                41, 52, 31, 37, 47, 55,
                30, 40, 51, 45, 33, 48,
                44, 49, 39, 56, 34, 53,
                46, 42, 50, 36, 29, 32 ] 

    key_56 = bitarray()
    key_56.frombytes(key)

    key_48 = bitarray([0 for i in range(48)])

    for i in range(48):
        key_48[i] = key_56[perm_2[i] - 1]
    
    return key_48.tobytes()

def xor(exp, key):
    xor_48 = bitarray([0 for i in range(48)])

    exp_48 = bitarray()
    exp_48.frombytes(exp)

    key_48 = bitarray()
    key_48.frombytes(key)

    for i in range(48):
        if exp_48[i] != key_48[i]:
            xor_48[i] = 1
    
    return xor_48.tobytes()

def divide_six_bits(bs_48):
    bits_48 = bitarray()
    bits_48.frombytes(bs_48)
    six_bits = []

    for i in range(8):
        six_bits.append(bits_48[i*6:(i+1)*6])
    
    return six_bits

def substitution(six_bits, table):
    index = six_bits.to01()
    n = table[index]
    n = "{0:b}".format(n)
    while len(n) < 4:
        n = '0' + n
    
    return bitarray(n)

def concat_substitution_result(list_subs):
    bits_32 = bitarray()
    for i in range(len(list_subs)):
        bits_32 += list_subs[i]
    
    return bits_32.tobytes()

def permutation(bs_32):
    perm = [16,  7, 20, 21, 29, 12, 28, 17,
             1, 15, 23, 26,  5, 18, 31, 10,
             2,  8, 24, 14, 32, 27,  3,  9,
            19, 13, 30,  6, 22, 11,  4, 25 ]
    
    bits_32 = bitarray()
    bits_32.frombytes(bs_32)

    perm_32 = bitarray([0 for i in range(32)])

    for i in range(32):
        perm_32[i] = bits_32[perm[i] - 1]
    
    return perm_32.tobytes()