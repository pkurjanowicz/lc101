import random

def makeKey(alphabet):
   alphabet = list(alphabet)
   random.shuffle(alphabet)
   return ''.join(alphabet)

def encrypt(plaintext, key, alphabet):
    keyMap = dict(zip(alphabet, key))
    return ''.join(keyMap.get(c.lower(), c) for c in plaintext)

def decrypt(cipher, key, alphabet):
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c.lower(), c) for c in cipher)

alphabet = "abcdefghijklmnopqrstuvwxyz? ,"
key = makeKey(alphabet)
plaintext = input("What do you want to encode?")
cipher = encrypt(plaintext, key, alphabet)

print(makeKey(alphabet))
#print(plaintext)
print(cipher)
print(decrypt(cipher, key, alphabet))

   
