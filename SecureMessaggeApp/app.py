# client.py
import socket
import threading

def create_client_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client_socket

def connect_to_server(client_socket, host, port):
    try:
        client_socket.connect((host, port))
        print(f"Connected to the server: {host}:{port}")
    except socket.error as e:
        print(f"Connection error: {e}")
        exit()

def get_user_credentials():
    username = input("Username: ")
    return username

def receive_messages(client_socket):
    try:
        while True:
            encrypted_message = client_socket.recv(1024).decode()
            if not encrypted_message:
                break
            decrypted_message = decrypt_message(encrypted_message)
            print(f"\nReceived Message: {decrypted_message}\nSend Message (type 'exit' to quit): ", end="")
    except Exception as e:
        print(f"Error (receiving messages): {e}")
    finally:
        client_socket.close()

def encrypt_message(message):
    # Simple Caesar cipher encryption
    key = 3
    encrypted_message = ''.join([chr((ord(char) + key)) for char in message])
    return encrypted_message

def decrypt_message(encrypted_message):
    # Simple Caesar cipher decryption
    key = 3
    decrypted_message = ''.join([chr((ord(char) - key)) for char in encrypted_message])
    return decrypted_message

def main():
    host = '192.168.1.110'
    port = 12345

    client_socket = create_client_socket()
    connect_to_server(client_socket, host, port)

    username = get_user_credentials()
    client_socket.send(username.encode())

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("Send Message (type 'exit' to quit): ")

        if message.lower() == 'exit':
            client_socket.close()
            exit()

        encrypted_message = encrypt_message(message)
        client_socket.send(encrypted_message.encode())

if __name__ == "__main__":
    main()
