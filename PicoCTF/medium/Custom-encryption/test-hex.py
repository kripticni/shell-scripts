text = "toyota trueno ae86"

def dynamic_xor_decrypt(ciphertext, text_key):
    plaintext = ""
    key_length = len(text_key)
    for i,char in enumerate(ciphertext):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        plaintext += encrypted_char
    plaintext = ''.join(reversed(plaintext))
    print(plaintext)
    return plaintext

def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    print(cipher_text)
    return cipher_text

cipher = dynamic_xor_encrypt(text,"trudeau")
clear = dynamic_xor_decrypt(cipher,"trudeau")
