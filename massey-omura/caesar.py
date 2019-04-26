
def encypher(data: bytearray, key: bytearray, decypher=False):
    '''
        Cifra/Decifra il messaggio, usando il metodo di Cesare e ruotando il chunk di key bytes

        Argomenti:
        - data: bytearray -> il chunk di dati
        - key: bytearray -> la chiave di cifratura/decifratura
        - decypher: boolean -> se vale True, si vuole decifrare (default: False)

        => Restituisce il messaggio cifrato/decifrato
    '''
    length = len(key)
    key = int.from_bytes(key, 'big')
    data = int.from_bytes(data, 'big')

    if not decypher:
        encoded = (data + key) % (pow(2, length * 8))
    else: encoded = (data - key) % (pow(2, length * 8))

    return bytearray(encoded.to_bytes(length, 'big'))
