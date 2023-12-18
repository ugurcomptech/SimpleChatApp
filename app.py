import socket

# İstemci soketini oluştur
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sunucu IP adresi ve port numarasını belirle
host = '0.0.0.0'  # Sunucu IP adresi
port = 12345

# Sunucuya bağlan
client_socket.connect((host, port))

while True:
    # Kullanıcıdan mesaj al
    message = input("Gönderilecek Mesaj: ")

    # Mesajı gönder
    client_socket.send(message.encode())

    # Sunucudan gelen yanıtı al ve ekrana yazdır
    data = client_socket.recv(1024).decode()
    print(f"Alınan Yanıt: {data}")
