import socket
import sys

host_ip="192.168.56.1"

client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect((host_ip,0))
except:
    print("Socket en uso")
    client_socket.close()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host_ip,0))
while True:
    print("Qué quiere decir? Escriba un mensaje y pulse enter")
    mensaje_cliente=input(str(">>"))
    if mensaje_cliente=="Salir":
        break
    else:
        mensaje_cliente=mensaje_clinte.encode()
        client_socket.send(mensaje_cliente)
        mensaje_servidor=client_socket.recv(1024).decode()
    continue

client_socket.close()
