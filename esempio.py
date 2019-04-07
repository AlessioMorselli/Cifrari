from cesare import Cesare
from permuta import Permuta
from cifrario import Cifrario
import sys
import re
import algoritmi

while True:
    cifra = False
    cesare = False

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
    print("   3) Esci")
    print("")
    scelta = input()

    if scelta == '1':
        cesare = True
    elif scelta == '3':
        break
    elif scelta != '2':
        print("Devi inserire un numero tra 1, 2 e 3")
        continue
    
    print("Inserire il file di input:")
    file_input = input()

    print("Inserire il file di output:")
    file_output = input()

    print("Operazione in corso...")

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

    print("Operazione terminata!")

print("Arrivederci!")
