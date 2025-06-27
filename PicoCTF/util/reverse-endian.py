def hex_to_bytes(hex_string: str) -> bytes:
    if hex_string.startswith(('0x', '0X')):
        hex_string = hex_string[2:]

    raw_bytes = bytes.fromhex(hex_string)

    return raw_bytes

def swap_endian(src: str) -> bytes:
    if src.startswith(('0x', '0X')):
        src = src[2:]

    if len(src) % 2 != 0:
        raise ValueError("Hexadecimal string must have an even number of characters.")

    dst = ''
    for i in range(len(src) - 2, -1, -2):
        dst += src[i:i+2] 

    dst = hex_to_bytes(dst)

    return dst        

string = "0x00000000004011a0"
print(swap_endian(string))
