cipher = input("Text to decipher: ")

result = ''
for c in cipher:
    if not c.isalpha():
        result = result + c
        continue
    if c.islower(): 
        neg = ord('a')
    else:
        neg = ord('A')

    result += chr(neg + (25 - (ord(c) - neg)))
print(result)
