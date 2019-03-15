import socket
import sys


host_ip="192.168.56.1"
port=8999
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((host_ip,port)
except:
    server_socket.close()
server_socket.listen(1)
print("Esperando conexiones")
conexion, addr_cliente=server_socket.accept()
print("Se ha conectado el usuario: ", addr_cliente)
while True:
    mensaje_cliente=conexion.recv(1024).decode()
    if mensaje_cliente == "Salir":
        break
    else:
        print(mensaje_cliente)
        print("Escriba una respuesta y pulse enter")
        mensaje_servidor=input(str(">>"))
        mensaje_servidor=mensaje_servidor.encode()
        conexion.send(mensaje_servidor)
    continue
server_socket.close()
