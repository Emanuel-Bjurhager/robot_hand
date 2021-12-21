
import socket

#roboRIO
IP = "172.22.11.2"
PORT = 1338
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP


#Read from component 2
UDP_IP = "127.0.0.1"
UDP_PORT = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
s.bind((UDP_IP, UDP_PORT))


# receive data from the server 
while 1:

    data = s.recv(1024)

    if data:
        print(data.decode('utf-8'))
        #Send open, half closed and closed hand
        sock.sendto(bytes(str(data.decode('utf-8')), "utf-8"), (IP, PORT))
    else:
        s.close()
        break
    #print('No more data')
    #s.close()
 


