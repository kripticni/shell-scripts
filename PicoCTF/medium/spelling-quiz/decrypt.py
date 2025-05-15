import itertools


def bruteforce(text):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    permutations = itertools.permutations(alphabet)

    for perm in permutations:
        dictionary = dict(zip(alphabet, perm))
        decrypted = "".join([dictionary[c] if c in dictionary else c for c in text])
        print(decrypted)


def derived(text):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    derived = list("XUNMRYDFWHGLSTIBJCAVOPEZQK".lower())
    dictionary = dict(zip(alphabet, derived))
    decrypted = "".join([dictionary[c] if c in dictionary else c for c in text])
    print(decrypted)


enc_flag = open("flag.txt", "r").read()
derived(enc_flag)
