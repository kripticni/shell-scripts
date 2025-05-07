import sys

ciphertext = open("ciphertext", "r").read()
# ciphertext = input()

lookup1 = '\n "#()*+/1:=[]abcdefghijklmnopqrstuvwxyz'
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"
# considering both of these are of length 40
# the first character will have no pervious so
# it is a direct lookup from 1 to 2
# for the rest of the characters the prev is
# the precalculated index for lookup1 in the last turn

plaintext = ""
prev = 0

for char in ciphertext:
    fcur = lookup2.index(char)
    cur = (fcur + prev) % 40
    dec = lookup1[cur]
    plaintext += dec
    prev = cur
    # print(f"{char} = {cur} =) {dec}")

sys.stdout.write(plaintext)
