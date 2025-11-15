import socket
import threading
import sys

# Server configuration
HOST = '127.0.0.1'
PORT = 12345

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'NICK':
                client_socket.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred!")
            client_socket.close()
            break

# Function to send messages to the server
def send_messages(client_socket):
    while True:
        message = input('')
        if message.lower() == 'quit':
            client_socket.close()
            sys.exit()
        else:
            client_socket.send(f'{nickname}: {message}'.encode('utf-8'))

# Main client function
def main():
    global nickname
    nickname = input("Enter your nickname: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Start threads for receiving and sending messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

if __name__ == "__main__":
    main()
