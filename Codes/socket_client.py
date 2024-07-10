import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.100.31', 5555)) #127.0.0.1
message = s.recv(1024)
s.close()

print(message.decode())