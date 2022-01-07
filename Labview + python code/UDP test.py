
import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 1337


print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP


while 1 == 1:

    #Send open, half closed and closed hand
    sock.sendto(bytes(str("0000000"), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(1)
    sock.sendto(bytes(str("0100000"), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(1)
    sock.sendto(bytes(str("1000000"), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(1)
    sock.sendto(bytes(str("0000000"), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(1)

    #Test every finger
    sock.sendto(bytes(str("1110000"), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(1)
    sock.sendto(bytes(str("1101000"), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(1)
    sock.sendto(bytes(str("1100100"), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(1)
    sock.sendto(bytes(str("1100010"), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(1)
    sock.sendto(bytes(str("1100001"), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(1)
    sock.sendto(bytes(str("0000000"), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(1)

    #Test in reverse
    sock.sendto(bytes(str("1100001"), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(1)
    sock.sendto(bytes(str("1100010"), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(1)
    sock.sendto(bytes(str("1100100"), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(1)
    sock.sendto(bytes(str("1101000"), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(1)
    sock.sendto(bytes(str("1110000"), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(1)


    sock.sendto(bytes(str("0000000"), "utf-8"), (UDP_IP, UDP_PORT)) #End with open
    time.sleep(2)
