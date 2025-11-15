import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

# List to keep track of connected clients
clients = []
nicknames = []

# Function to broadcast messages to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Remove the client if sending fails
                remove_client(client)

# Function to handle individual client connections
def handle_client(client_socket):
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024)
            if message:
                # Broadcast the message to other clients
                broadcast(message, client_socket)
            else:
                # Client disconnected
                remove_client(client_socket)
                break
        except:
            # Client disconnected
            remove_client(client_socket)
            break

# Function to remove a client from the list
def remove_client(client_socket):
    if client_socket in clients:
        index = clients.index(client_socket)
        clients.remove(client_socket)
        nickname = nicknames[index]
        nicknames.remove(nickname)
        broadcast(f'{nickname} left the chat!'.encode('utf-8'), client_socket)
        client_socket.close()

# Main server function
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        print(f"Connected with {client_address}")

        # Request nickname
        client_socket.send('NICK'.encode('utf-8'))
        nickname = client_socket.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client_socket)

        print(f"Nickname of the client is {nickname}")
        broadcast(f'{nickname} joined the chat!'.encode('utf-8'), client_socket)
        client_socket.send('Connected to the server!'.encode('utf-8'))

        # Start a new thread for the client
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    main()
