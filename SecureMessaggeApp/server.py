# server.py
import socket
import threading

users = {}

def handle_client(client_socket, username):
    try:
        while True:
            encrypted_message = client_socket.recv(1024).decode()
            if not encrypted_message:
                break
            print(f"Received Encrypted Message ({username}): {encrypted_message}")

            decrypted_message = decrypt_message(encrypted_message)
            print(f"Decrypted Message ({username}): {decrypted_message}")

            broadcast_message = f"({username}): {decrypted_message}"
            broadcast_to_all(broadcast_message, client_socket)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        remove_user(username, client_socket)

def broadcast_to_all(message, sender_socket):
    for user, client in users.items():
        if client != sender_socket:
            try:
                client.send(encrypt_message(message).encode())
            except Exception as e:
                print(f"Error (broadcast): {e}")

def remove_user(username, client_socket):
    if username in users:
        del users[username]
        print(f"{username} connection closed.")

def encrypt_message(message):
    key = 3
    encrypted_message = ''.join([chr((ord(char) + key)) for char in message])
    return encrypted_message

def decrypt_message(encrypted_message):
    key = 3
    decrypted_message = ''.join([chr((ord(char) - key)) for char in encrypted_message])
    return decrypted_message

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.1.110', 12345))
    server_socket.listen(5)
    print("Server listening...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"New connection: {addr}")

        if addr[0] not in users:
            client_socket.send("Enter your username: ".encode())
            username = client_socket.recv(1024).decode()
            users[username] = client_socket
            print(f"{username} joined.")

            client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
            client_thread.start()

if __name__ == "__main__":
    main()
