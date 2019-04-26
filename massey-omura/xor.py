
def encypher(data: bytearray, key: bytearray):
    xor_bytes = [d ^ k for d, k in zip(data, key)]
    return bytearray(xor_bytes)