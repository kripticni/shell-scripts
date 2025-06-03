import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        print(binary)
        # print(c)
        print(binary[:4])
        print(binary[4:])
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc


def b16_decode(cipher):
    dec = ""
    for i in range(0, len(cipher), 2):
        binary1 = "{0:08b}".format(ALPHABET.index(cipher[i]))
        binary2 = "{0:08b}".format(ALPHABET.index(cipher[i + 1]))
        print(binary1[4:], binary2[4:])
        char = chr(int(binary1[4:] + binary2[4:], 2))
        dec += char
    return dec


# so if we stick the two together
# we can derive the original character
# also considering the 4 bits can only
# have upto 16 combinations, it makes sense
# why the alphabet is actually the first 16 chars

print(ALPHABET)
print(b16_encode("picoctf"))
print(b16_decode(b16_encode("picoctf")))
