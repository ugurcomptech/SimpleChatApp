import socket
import sys
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
        sys.exit()

def send_message(client_socket, message):
    # Mesajı gönder
    client_socket.send(message.encode())

def receive_response(client_socket):
    # Sunucudan gelen yanıtı al ve ekrana yazdır
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Alınan Yanıt: {data}")

def close_connection(client_socket):
    # Bağlantıyı kapat
    client_socket.close()
    print("Bağlantı kapatıldı.")
    sys.exit()

def main():
    # Sunucu IP adresi ve port numarasını belirle
    host = '0.0.0.0'  # Sunucu IP adresi
    port = 12345

    client_socket = create_client_socket()
    connect_to_server(client_socket, host, port)

    # Sunucudan gelen mesajları dinleme işlemi için bir thread başlat
    receive_thread = threading.Thread(target=receive_response, args=(client_socket,))
    receive_thread.start()

    while True:
        # Kullanıcıdan mesaj al
        message = input("Gönderilecek Mesaj (exit yazarak çıkış yapabilirsiniz): ")

        if message.lower() == 'exit':
            close_connection(client_socket)

        # Mesaj gönderme
        send_message(client_socket, message)

if __name__ == "__main__":
    main()
