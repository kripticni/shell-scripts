def generator(g,x,p):
    return pow(g,x) % p

def dynamic_xor_decrypt(ciphertext, text_key):
    plaintext = ""
    key_length = len(text_key)
    for i,char in enumerate(ciphertext):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        plaintext += encrypted_char
    plaintext = ''.join(reversed(plaintext))
    #print(plaintext)
    return plaintext

def decrypt(ciphertext, key):
    plain = []
    for num in ciphertext:
        plain.append(chr(num // (key*311)))
    return plain

p = 97
g = 31

a = range(87,97)
b = range(21,31)

u = [generator(g,i,p) for i in a]
v = [generator(g,i,p) for i in b]

a_key = []
for i in v:
    for j in a:
        a_key.append((generator(i,j,p),i,j))

b_key = []
for i in u:
    for j in b:
        b_key.append((generator(i,j,p),i,j))

key = []
args = []

for i in range(len(a_key)):
    if a_key[i][0] == b_key[i][0]:
        key.append(a_key[i][0])
        args.append((a_key[i][2],b_key[i][2],a_key[i][1],b_key[i][1]))

ciphertext = [33588, 276168, 261240, 302292, 343344, 328416, 242580, 85836, 82104, 156744, 0, 309756, 78372, 18660, 253776, 0, 82104, 320952, 3732, 231384, 89568, 100764, 22392, 22392, 63444, 22392, 97032, 190332, 119424, 182868, 97032, 26124, 44784, 63444]

for i in key:
    semiplain = decrypt(ciphertext,i)
    plain = dynamic_xor_decrypt(semiplain,"trudeau")
    if plain.startswith("pico"):
        print(plain)

#reminds awfully of diffie hellman doesnt it

