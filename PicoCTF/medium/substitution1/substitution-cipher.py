import string

def generate_key(shift):
    alphabet = string.ascii_uppercase
    return str.maketrans(alphabet, alphabet[shift:] + alphabet[:shift])

def decrypt(ciphertext, key):
    return ciphertext.translate(key)

choice = input("Shift? [y/n] ").strip().upper()

if choice == "Y":
    shift = int(input("Enter the shift value: ").strip())
    key = generate_key(shift)
else:
    key_str = input("Enter the 26: ").strip().upper()
    if len(key_str) != 26 or not set(key_str).issubset(set(string.ascii_uppercase)):
        print("Invalid key format.")
        exit()
    key = str.maketrans(key_str, string.ascii_uppercase)

ciphertext = input("Enter the ciphertext: ").strip().upper()
plaintext = decrypt(ciphertext, key)

print("Decrypted text:", plaintext)
