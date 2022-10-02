import socket
import threading

def handle_client(conn, addr):
    while True:
        msg_length = conn.recv(64).decode("utf-8")
        if msg_length:
           msg = conn.recv(int(msg_length)).decode('utf-8')
           print(msg)

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname(socket.gethostname()), 5050))

start()