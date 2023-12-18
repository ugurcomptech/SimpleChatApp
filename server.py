import socket

# Sunucu soketini oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sunucu IP adresi ve port numarasını belirle
host = '0.0.0.0'  # Host IP
port = 12345

# Sunucu soketini belirtilen IP ve port numarasına bağla
server_socket.bind((host, port))

# Bağlantıları dinle
server_socket.listen()

print(f"Sunucu {host}:{port} üzerinde dinleniyor...")

# İstemci bağlantısını kabul et
client_socket, client_address = server_socket.accept()
print(f"{client_address} bağlandı.")

while True:
    # İstemciden gelen veriyi al ve ekrana yazdır
    data = client_socket.recv(1024).decode()
    print(f"Alınan Mesaj: {data}")

    # İstemciden mesaj alındıktan sonra yeni mesaj göndermek için kullanıcıdan giriş al
    new_message = input("Gönderilecek Mesaj: ")
    client_socket.send(new_message.encode())
