from generate_prime import generate_prime
import exp_mod, xor, caesar

with open("tiger.bmp", "rb") as f:
    header = f.read(54)
    picture = f.read()

length = 512
n_bytes = length // 8
additional_bytes = len(picture) % n_bytes

p = generate_prime(length)
p_bytes = p.to_bytes(n_bytes, 'big')
result = b''

ea, da = exp_mod.generate_keys(p_bytes)

### --- Test di cifratura --- ###
for i in range(additional_bytes):
    picture += b'\x00'

for i in range(len(picture) // n_bytes):
    #result += xor.encypher(picture[i*n_bytes : (i+1)*n_bytes], p_bytes)
    result += caesar.encypher(picture[i*n_bytes : (i+1)*n_bytes], p_bytes)
    #result += exp_mod.encypher(p_bytes, ea, picture[i*n_bytes : (i+1)*n_bytes])

for i in range(additional_bytes):
    result =  result[:-1]

encoded = header + result
with open("enctest.bmp", "wb") as f:
    f.write(encoded)

### --- Test di decifratura --- ###
for i in range(additional_bytes):
    result += b'\x00'

decoded = b''
for i in range(len(result) // n_bytes):
    #decoded += xor.encypher(result[i*n_bytes : (i+1)*n_bytes], p_bytes)
    decoded += caesar.encypher(result[i*n_bytes : (i+1)*n_bytes], p_bytes, decypher=True)
    #decoded += exp_mod.encypher(p_bytes, da, result[i*n_bytes : (i+1)*n_bytes])

for i in range(additional_bytes):
    decoded =  decoded[:-1]

decoded = header + decoded
with open("dectest.bmp", "wb") as f:
    f.write(decoded)
