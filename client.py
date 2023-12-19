import socket
import threading

def create_client_socket():
    # İstemci soketini oluştur
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return client_socket

def connect_to_server(client_socket, host, port):
    # Sunucuya bağlan
    try:
        client_socket.connect((host, port))
        print(f"Sunucuya bağlandı: {host}:{port}")
    except socket.error as e:
        print(f"Bağlantı hatası: {e}")
        exit()

def get_user_credentials():
    # Kullanıcı adını al
    username = input("Kullanıcı Adı: ")
    return username

def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"\nAlınan Mesaj: {message}\nGönderilecek Mesaj (exit yazarak çıkış yapabilirsiniz): ", end="")
    except Exception as e:
        print(f"Hata (alınan mesajlar): {e}")
    finally:
        client_socket.close()

def main():
    # Sunucu IP adresi ve port numarasını belirle
    host = '0.0.0.0'  # Sunucu IP adresi
    port = 12345

    client_socket = create_client_socket()
    connect_to_server(client_socket, host, port)

    # Kullanıcı adını sunucuya gönder
    username = get_user_credentials()
    client_socket.send(username.encode())

    # Sunucudan gelen mesajları dinleme işlemi için yeni bir thread başlat
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        # Kullanıcıdan mesaj al
        message = input("Gönderilecek Mesaj (exit yazarak çıkış yapabilirsiniz): ")

        if message.lower() == 'exit':
            client_socket.close()
            exit()

        # Mesajı gönder
        client_socket.send(message.encode())

if __name__ == "__main__":
    main()
