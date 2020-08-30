from sys import exit
from pyshark import FileCapture

packets = None
try:
    packets = FileCapture("files/home.pcapng")
except Exception as e:
    print("===== Datei kann nicht eingelesen =====")
    exit(0)

#for packet in packets:
    #print(packet)
packets.close()
