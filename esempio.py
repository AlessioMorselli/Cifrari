from cesare import Cesare
from permuta import Permuta
from cifrario import Cifrario
from feistel import Feistel
from feistel import FeistelFunctions
import sys
import re
import algoritmi

while True:
    cifra = False
    cesare = False
    feistel = False

    print("Si vuole cifrare o decifrare?")
    print("   1) Cifrare")
    print("   2) Decifrare")
    print("   3) Esci")
    print("")
    scelta = input()

    if scelta == '1':
        cifra = True
    elif scelta == '3':
        break
    elif scelta != '2':
        print("Devi inserire un numero tra 1, 2 e 3")
        continue
    
    print("Quale metodo usare?")
    print("   1) Cesare")
    print("   2) Permutazione")
    print("   3) Feistel")
    print("   4) Esci")
    print("")
    scelta = input()

    if scelta == '1':
        cesare = True
    if scelta == '3':
        feistel = True
    elif scelta == '4':
        break
    elif scelta != '2':
        print("Devi inserire un numero tra 1, 2 e 3")
        continue
    
    print("Inserire il file di input:")
    file_input = input()

    try:
        f = open(file_input, "r")
        f.close()
    except IOError:
        print("Il file indicato non esiste! Riprovare...")
        continue

    print("Inserire il file di output:")
    file_output = input()

    try:
        f = open(file_output, "w")
        f.close()
    except IOError:
        print("Il file indicato non esiste! Riprovare...")
        continue

    print("Operazione in corso...")

    if not feistel:
        if cifra:
            if cesare:
                cifrario = Cifrario(Cesare())
            else:
                cifrario = Cifrario(Permuta())
            
            text = algoritmi.encipher(file_input, cifrario)
        else:
            if cesare:
                cifrario = Cifrario(Cesare())

                text = algoritmi.cesare_decipher(file_input, cifrario)
            else:
                cifrario = Cifrario(Permuta())

                text = algoritmi.permuta_decipher(file_input, cifrario)
        
        with open(file_output, "w") as f:
            f.write(text)
    else:
        times = 10
        if cifra:
            feistel = Feistel()
            picture = algoritmi.feistel_encipher(file_input, feistel, times, [i for i in range(1, times + 1)])
        else:
            feistel = Feistel(True)
            picture = algoritmi.feistel_encipher(file_input, feistel, times, [i for i in range(times, 0, -1)])

        with open(file_output, "wb") as f:
            f.write(picture)

    print("Operazione terminata!")

print("Arrivederci!")
