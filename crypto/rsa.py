def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

p = 137
q = 131
n = p * q
r = (p - 1) * (q -1)
e = 3
d = modinv(e, r)
m = 513
c =  (m ** e ) % n
mp = (c **d  ) % n
dP = d % (p - 1)
dQ = d % (q - 1)
qInv = modinv(q, p) % p
sP = (c ** dP) % p
sQ = (c ** dQ) % q
h = qInv *(sP - sQ) % p
mp2 = sQ + h * q
pInv = modinv(p, q) % q

print("RSA values")
print(f"p = {p} q = {q} \nn = p * q = {p} * {q} = {n}")
print(f"e = {e} d = {d}\n")

print(f"Message = {m}\n")

print(f"Encrypt: m^e mod n")
print(f"Encrypted message: {m}^{e} mod {n} = {c}\n")
print("Decrypt message: c^d mod n")
print(f"m = {c}^{d} mod {n} = {mp}\n")

print("RSA CRT values")
print(f"dP = d mod (p - 1) = {d} mod ({p} - 1) = {dP}")
print(f"dQ = d mod (q - 1) = {d} mod ({q} - 1) = {dQ}")
print(f"qInv = q^-1 mod p = {q}^-1 mod {p} = {qInv}")
print(f"sP = enc^dP mod p = {c}^{dP} mod {p} = {sP}")
print(f"sQ = enc^dQ mod q = {c}^{dQ} mod {q} = {sQ}")

print(f"h = q^-1 (sP * sQ) mod p = {qInv} * ({sP} - {sQ}) mod {p} = {h}")
print(f"m = sQ + h * q = {sQ} + {h} * {q} = {mp2}\n")

mGau =  (sP * q *(qInv %p) + sQ*p*(pInv % q)) % n
mGar =  sQ + q * ((sP-sQ)* (qInv %p) %p)

print("Gauss = m = (sP * q * (q^-1 mod p) + sQ * p * (p^-1 mod q)) mod n")
print(f"Gauss = {mGau} =  ({sP} * {q} *({qInv} % {p}) + {sQ} *{p} *({pInv} % {q})) % {n}\n")
print("Garner = m = sQ + q *((sP - sQ) * (q^-1 mod p) mod p)")
print(f"Garner = {mGar} =  {sQ} + {q} * (({sP}-{sQ}) * ({qInv} % {p}) % {p})")
