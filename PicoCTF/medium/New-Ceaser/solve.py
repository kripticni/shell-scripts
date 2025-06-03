import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_decode(cipher):
    dec = ""
    for i in range(0, len(cipher) - 1, 2):
        # print(cipher[i], i, cipher[i + 1], i + 1)
        binary1 = "{0:08b}".format(ALPHABET.index(cipher[i]))
        binary2 = "{0:08b}".format(ALPHABET.index(cipher[i + 1]))
        # print(binary1[4:], binary2[4:])
        char = chr(int(binary1[4:] + binary2[4:], 2))
        dec += char
    return dec


def unshift(c, k):
    t1 = ord(c) + LOWERCASE_OFFSET
    t2 = ord(k) + LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


b16 = open("ciphertext.txt", "r").read()
key = ALPHABET

# assert len(key) == 1
# assert all([k in ALPHABET for k in key])
# from these asserts we can figure out
# that the key is a single letter from
# the ALPHABET list

for k in key:
    dec = ""
    for i, c in enumerate(b16):
        dec += unshift(c, k)
    cleartext = b16_decode(dec)
    filtered = "".join([char for char in cleartext if char.isascii()])
    # print(len(dec))
    # print(filtered, len(filtered))
    if len(filtered) == len(dec) // 2:
        print(cleartext)
