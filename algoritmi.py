import random
import re
from cifrario import Cifrario
from cesare import Cesare
from permuta import Permuta
from feistel import Feistel

def encipher(file, cifrario):
    new_lines = []
    new_words = []

    with open(file, "r") as f:
        for line in f.readlines():
            new_words += cifrario.add_to_dictionary(line)
            new_lines.append(cifrario.encipher(line))
    
    cifrario.write_new_words(new_words)

    return ''.join(new_lines)

def cesare_decipher(file, cifrario):
    # Decido un numero casuale di righe da controllare
    n_lines = random.randint(20, 50)
    max_count = 0
    right_offset = -1

    for offset in range(1, 26):
        new_lines = []
        count = 0
        i = 0

        cifrario.new_method(Cesare(offset))

        with open(file, "r") as f:
            for line in f.readlines():
                i += 1
                new_lines.append(cifrario.encipher(line, True))
                count += cifrario.count_words(new_lines[-1])
                if i > n_lines:
                    break
        
        print("Offset: " + str(offset) + " - Count: " + str(count))
        if count > max_count:
            max_count = count
            right_offset = offset

    deciphered_lines = []
    cifrario.new_method(Cesare(right_offset))

    with open(file, "r") as f:
        for line in f.readlines():
            deciphered_lines.append(cifrario.encipher(line, True))
        
    return ''.join(deciphered_lines)

def permuta_decipher(file, cifrario):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_dictionary = {}
    for c in alfabeto:
        alfabeto_dictionary[c] = 0

    with open(file, "r") as f:
        for line in f.readlines():
            tmp = cifrario.count_characters(line)
            for c in alfabeto:
                alfabeto_dictionary[c] += tmp[c]
    
    deciphered_alfabeto = cifrario.compares_characters(alfabeto_dictionary)
    cifrario.new_method(Permuta(deciphered_alfabeto, False))

    deciphered_lines = []
    with open(file, "r") as f:
        for line in f.readlines():
            deciphered_lines.append(cifrario.encipher(line, True))
        
    return ''.join(deciphered_lines)

def feistel_encipher(file, feistel, keys):
    with open(file, "rb") as f:
        header = f.read(54)
        picture = f.read()
    
    for k in keys:
        picture = feistel.encipher(picture, k)
    
    return header + picture