from feistel import Feistel
from des import expansion, xor, subtable, substitution, permutation, permuted_choice_1
from des import rotate_key, permuted_choice_2, divide_six_bits, concat_substitution_result
import sys

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

def create_keys(key):
    keys = []
    key_56 = permuted_choice_1(key)
    for i in range(16):
        rotated_key = rotate_key(key_56, i)
        keys.append(permuted_choice_2(rotated_key))
    
    return keys

if sys.argv[1] == 'e':
    file_input = "img.bmp"
    file_output = "enc.bmp"
    decipher = False
elif sys.argv[1] == 'd':
    file_input = "enc.bmp"
    file_output = "dec.bmp"
    decipher = True
    
with open(file_input, "rb") as f:
    header = f.read(54)
    picture = f.read()
feistel = Feistel(function=des, decipher=decipher)    

key = []
with open("key", "r") as f:
    for line in f.readlines():
        key.append(int(line))
key = bytes(key)

keys = create_keys(key)
enc = picture

if sys.argv[1] == 'e':
    for i in range(16):
        print("Iterazione " + str(i + 1) + " su 16 in corso...")
        enc = feistel.encipher(enc, keys[i])
        print("Iterazione " + str(i + 1) + " su 16 completata")
elif sys.argv[1] == 'd':
    feistel = Feistel(function=des, decipher=True)
    for i in range(15, -1, -1):
        print("Iterazione " + str(i + 1) + " su 16 in corso...")
        enc = feistel.encipher(enc, keys[i])
        print("Iterazione " + str(i + 1) + " su 16 completata")

with open(file_output, "wb") as f:
    f.write(header + enc)