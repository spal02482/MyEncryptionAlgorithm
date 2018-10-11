from runlength import rlencode, rldecode
from bw import transform, inverseTransform
from cipher import encipher, decipher

data = input()
key = input()

[data, first] = transform(data)
data = rlencode(data)
data = encipher(data, key, first)

print("\nEncrypted Data:", data, '\n')

data = decipher(data, key, first)
data = rldecode(data)
data = inverseTransform(data, first)

print("\nDecrypted Data:", data, '\n')