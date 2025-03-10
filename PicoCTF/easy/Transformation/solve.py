enc_text = str(open("enc", "r").read())

decoded = ''.join([
    chr(ord(c) >> 8) + chr(ord(c) & 0xFF)
    for c in enc_text
])

print(decoded)
