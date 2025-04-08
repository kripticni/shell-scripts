def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(a, m):
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"Modular inverse does not exist for {a} modulo {m}")
    return x % m


numbers = [
    268,
    413,
    438,
    313,
    426,
    337,
    272,
    188,
    392,
    338,
    77,
    332,
    139,
    113,
    92,
    239,
    247,
    120,
    419,
    72,
    295,
    190,
    131,
]

modulus = 41

for num in numbers:
    mod_num = num % modulus
    try:
        inverse = mod_inverse(mod_num, modulus)
        # print(f"mod_inverse({mod_num}, {modulus}) = {inverse}")
        if inverse < 27:
            char = chr(ord("a") + inverse - 1)
        elif inverse < 37:
            char = chr(ord("0") + inverse - 27)
        elif inverse == 37:
            char = "_"
        print(char, end="")
    except ValueError as e:
        print(e)
