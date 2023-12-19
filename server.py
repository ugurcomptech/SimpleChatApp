import socket
import threading

# Sunucu soketini oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sunucu IP adresi ve port numarasını belirle
host = '0.0.0.0'  # Tüm ağ arayüzlerine açık olacak şekilde
port = 12345

# Sunucu soketini belirtilen IP ve port numarasına bağla
server_socket.bind((host, port))

# Bağlantıları dinle
server_socket.listen()

print(f"Sunucu {host}:{port} üzerinde dinleniyor...")

# Bağlı istemci bilgilerini tutmak için bir sözlük
clients = {}

def handle_client(client_socket, client_address):
    while True:
        # İstemciden gelen veriyi al
        data = client_socket.recv(1024).decode()

        # İstemciden gelen veriyi diğer istemcilere ileti
        for other_client_socket in clients.values():
            if other_client_socket != client_socket:
                other_client_socket.send(f"{client_address}: {data}".encode())

# İstemci bağlantılarını kabul et ve her biri için bir iş parçacığı başlat
while True:
    client_socket, client_address = server_socket.accept()
    print(f"{client_address} bağlandı.")

    # Yeni bir iş parçacığı başlat ve istemci bağlantısını işlemek üzere fonksiyona yönlendir
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

    # Bağlı istemcileri takip etmek için sözlüğe ekle
    clients[client_socket] = client_socket
