import socket
import threading

users = {}  # Kullanıcıları saklamak için sözlük: {username: client_socket}

def handle_client(client_socket, username):
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"Alınan Mesaj ({username}): {message}")
            
            # Sunucuya gelen mesajları diğer kullanıcılara iletme (broadcast)
            broadcast_message = f"({username}): {message}"
            broadcast_to_all(broadcast_message, client_socket)
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        remove_user(username, client_socket)

def broadcast_to_all(message, sender_socket):
    for user, client in users.items():
        if client != sender_socket:
            try:
                client.send(message.encode())
            except Exception as e:
                print(f"Hata (broadcast): {e}")

def remove_user(username, client_socket):
    if username in users:
        del users[username]
        print(f"{username} bağlantısı kapatıldı.")
        # broadcast_to_all(f"{username} ayrıldı.", client_socket)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(5)
    print("Sunucu dinleme başladı...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Yeni bağlantı: {addr}")

        # Kullanıcı adını bir kez iste
        if addr[0] not in users:  # Kullanıcı daha önce bağlanmamışsa
            client_socket.send("Kullanıcı adınızı girin: ".encode())
            username = client_socket.recv(1024).decode()
            users[username] = client_socket
            print(f"{username} katıldı.")

            # Kullanıcıya gelen mesajları dinleme işlemi için yeni bir thread başlat
            client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
            client_thread.start()

if __name__ == "__main__":
    main()
