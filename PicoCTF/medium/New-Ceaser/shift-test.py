import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


def unshift(c, k):
    t1 = ord(c) + LOWERCASE_OFFSET
    t2 = ord(k) + LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


key = "redacted"
b16 = "picoctf"
print(
    string.ascii_lowercase.index("t")
)  # the t in picoctf wraps around by 3 because its
# the 19th index and this only works up to 16
enc = ""
dec = ""
for i, c in enumerate(b16):
    enc += shift(c, key[i % len(key)])
print(enc)

for i, c in enumerate(enc):
    dec += unshift(c, key[i % len(key)])
print(dec)
