numbers = [
    128,
    322,
    353,
    235,
    336,
    73,
    198,
    332,
    202,
    285,
    57,
    87,
    262,
    221,
    218,
    405,
    335,
    101,
    256,
    227,
    112,
    140,
]

modulus = 37

for num in numbers:
    mod_num = num % modulus
    if mod_num < 26:
        char = chr(ord("A") + mod_num)
    elif mod_num < 36:
        char = chr(ord("0") + mod_num - 26)
    elif mod_num == 36:
        char = "_"
    print(char, end="")
