import sys
import socket
LISTEN_PORT=int(sys.argv[1])

addr=('127.0.0.1', LISTEN_PORT)
sock=socket.create_connection(addr)
sock.sendall(bytes("stop".encode("utf-8")))
sock.close()
