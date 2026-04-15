import socket
import threading

HOST = '127.0.0.1'
PORT = 5555
clients = []

def broadcast(message, _client):
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                client.close()
                if client in clients: clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(2048)
            if not message: break
            broadcast(message, client)
        except:
            break
    if client in clients: clients.remove(client)
    client.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Port busy error fix
    server.bind((HOST, PORT))
    server.listen()
    print(f"[*] CORE SERVER ACTIVE ON {HOST}:{PORT}...")
    while True:
        client, addr = server.accept()
        print(f"[*] Node Connected: {addr}")
        clients.append(client)
        threading.Thread(target=handle_client, args=(client,), daemon=True).start()

if __name__ == "__main__":
    start_server()
