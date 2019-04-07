from cifrario import Cifrario
from cesare import Cesare
import sys

cifrario = Cifrario(Cesare())
alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_dictionary = {}

with open("lettere.txt", "r") as f:
    i = 0
    for line in f.readlines():
        alfabeto_dictionary[alfabeto[i]] = int(line)
        i += 1

with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        tmp = cifrario.count_characters(line)
        for c in alfabeto:
            alfabeto_dictionary[c] += tmp[c]
    
with open("lettere.txt", "w") as f:
    for v in alfabeto_dictionary.values():
        f.write(str(v) + '\n')
