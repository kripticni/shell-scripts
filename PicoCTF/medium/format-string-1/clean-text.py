fd = open("cleanhex.txt", 'r')
hex_data = fd.read().split()

for hex_value in hex_data:
    if hex_value.startswith("0x"):
        hex_value = hex_value[2:] 
        
        try:
            string = bytes.fromhex(hex_value).decode('latin1')
            print(f"{string[::-1]}")
        except ValueError:
            print(f"Invalid hex value: {hex_value}")
    else:
        print(f"Skipping invalid value: {hex_value}")
