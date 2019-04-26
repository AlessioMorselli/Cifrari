from random import getrandbits
from sympy.ntheory.primetest import isprime
import time

def generate_prime(length: int):
    """ Genera un numero primo composto dal numero di bit indicato

        Argomenti:
        - length: int -> numero di bit di cui deve essere composto il primo

        => Restituisce un numero primo
    """
    #start = time.time()
    #i = 1
    while True:
        # Genero una stringa casuale di bit lunga 'length'
        p = getrandbits(length)
        # Applico una maschera in modo che il primo e l'ultimo bit valgano 1
        p |= (1 << length - 1) | 1

        #print(i)
        #i += 1

        if isprime(p):
            break

    #print("Prime generated in: " + str(time.time() - start))
    return p