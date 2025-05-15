import itertools


def bruteforce(text):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    permutations = itertools.permutations(alphabet)

    for perm in permutations:
        dictionary = dict(zip(perm, alphabet))
        cleartext = "".join([dictionary[c] if c in dictionary else c for c in text])
        print(cleartext)


def derived(text):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    derived = list("XUNMRYDFWHGLSTIBJCAVOPEZQK".lower())
    dictionary = dict(zip(derived, alphabet))
    cleartext = "".join([dictionary[c] if c in dictionary else c for c in text])
    print(cleartext)


enc_flag = open("flag.txt", "r").read()
derived(enc_flag)
