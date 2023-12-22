# client.py
import socket
import threading

def create_client_socket():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client_socket

def connect_to_server(client_socket, host, port):
    try:
        client_socket.connect((host, port))
        print(f"Sunucuya bağlandı: {host}:{port}")
    except socket.error as e:
        print(f"Bağlantı hatası: {e}")
        exit()

def get_user_credentials():
    username = input("Kullanıcı Adı: ")
    return username

def get_room_name():
    room_name = input("Oda Adı: ")
    return room_name

def receive_messages(client_socket):
    try:
        while True:
            encrypted_message = client_socket.recv(1024).decode()
            if not encrypted_message:
                break
            decrypted_message = decrypt_message(encrypted_message)
            print(f"\nAlınan Mesaj: {decrypted_message}\nMesaj Gönder (çıkmak için 'exit' yazın): ", end="")
    except Exception as e:
        print(f"Hata (mesajları alma): {e}")
    finally:
        client_socket.close()

def encrypt_message(message):
    key = 3
    encrypted_message = ''.join([chr((ord(char) + key)) for char in message])
    return encrypted_message

def decrypt_message(encrypted_message):
    key = 3
    decrypted_message = ''.join([chr((ord(char) - key)) for char in encrypted_message])
    return decrypted_message

def main():
    host = '192.168.1.110'
    port = 12345

    client_socket = create_client_socket()
    connect_to_server(client_socket, host, port)

    username = get_user_credentials()
    room_name = get_room_name()

    client_socket.send(username.encode())
    client_socket.send(room_name.encode())

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("Mesaj Gönder (çıkmak için 'exit' yazın): ")

        if message.lower() == 'exit':
            client_socket.close()
            exit()

        encrypted_message = encrypt_message(message)
        client_socket.send(encrypted_message.encode())

if __name__ == "__main__":
    main()
