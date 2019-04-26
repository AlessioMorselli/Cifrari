from random import getrandbits
from math import gcd
from solve_linear_congruence import solve_linear_congurence

def generate_keys(prime: bytearray):
    '''
        Genera la chiave di cifratura e decifratura per il crittosistema di Massey-Omura

        Argomenti:
        - prime: bytearray -> il primo su cui si basa il crittosistema

        => Restituisce un array di questo tipo: [encryption, decryption]
    '''
    prime = int.from_bytes(prime, 'big')
    length = len("{0:b}".format(prime))
    while True:
        # Genero una stringa casuale di bit lunga 'length'
        e = getrandbits(length)

        if gcd(e, prime - 1) == 1 and e != prime:
            break
    
    d = solve_linear_congurence(e, 1, prime - 1)

    return bytearray(e.to_bytes(length // 8, 'big')), bytearray(d.to_bytes(length // 8, 'big'))

def encypher(prime: bytearray, key: bytearray, msg: bytearray):
    '''
        Cifra/Decifra il messaggio, usando la chiave e il primo indicati
        Il messaggio deve essere: 1 < msg < prime

        Argomenti:
        - prime: bytearray -> il primo su cui si basa il crittosistema
        - key: bytearray -> la chiave di cifratura/decifratura
        - msg: bytearray -> il messaggio da cifrare

        => Restituisce il messaggio cifrato/decifrato o None se il messaggio non rispetta la condizione
    '''
    length = len(msg)
    prime = int.from_bytes(prime, 'big')
    msg = int.from_bytes(msg, 'big')
    key = int.from_bytes(key, 'big')

    if msg <= 1 or msg >= prime:
        return None
    else:
        enc = pow(msg, key, prime)
        return bytearray(enc.to_bytes(length, 'big'))