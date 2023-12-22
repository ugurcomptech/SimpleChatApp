# server.py
import socket
import threading

# Kullanıcıları depolamak için bir sözlük
users = {}

def handle_client(client_socket, username):
    try:
        while True:
            # Şifreli mesajı al, çöz ve ekrana yazdır
            encrypted_message = client_socket.recv(1024).decode()
            if not encrypted_message:
                break
            print(f"Şifreli Mesaj Alındı ({username}): {encrypted_message}")

            decrypted_message = decrypt_message(encrypted_message)
            print(f"Çözülmüş Mesaj ({username}): {decrypted_message}")

            # Yayınlanacak mesajı oluştur ve tüm kullanıcılara gönder
            broadcast_message = f"({username}): {decrypted_message}"
            broadcast_to_all(broadcast_message, client_socket)
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        # Kullanıcıyı kaldır
        remove_user(username, client_socket)

def broadcast_to_all(message, sender_socket):
    # Tüm kullanıcılara mesajı gönder
    for user, client in users.items():
        if client != sender_socket:
            try:
                client.send(encrypt_message(message).encode())
            except Exception as e:
                print(f"Hata (yayın): {e}")

def remove_user(username, client_socket):
    # Kullanıcıyı kaldır
    if username in users:
        del users[username]
        print(f"{username} bağlantısı kapatıldı.")

def encrypt_message(message):
    # Basit bir Caesar şifreleme uygula
    key = 3
    encrypted_message = ''.join([chr((ord(char) + key)) for char in message])
    return encrypted_message

def decrypt_message(encrypted_message):
    # Basit bir Caesar şifre çözme uygula
    key = 3
    decrypted_message = ''.join([chr((ord(char) - key)) for char in encrypted_message])
    return decrypted_message

def main():
    # Sunucu soketi oluştur ve belirtilen IP adresi ve port numarasında dinle
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.1.110', 12345))
    server_socket.listen(5)
    print("Sunucu dinleniyor...")

    while True:
        # Yeni bir istemci bağlantısı kabul et
        client_socket, addr = server_socket.accept()
        print(f"Yeni bağlantı: {addr}")

        # Eğer IP adresi daha önce kaydedilmemişse kullanıcı adını iste ve kaydet
        if addr[0] not in users:
            client_socket.send("Kullanıcı adınızı girin: ".encode())
            username = client_socket.recv(1024).decode()
            users[username] = client_socket
            print(f"{username} katıldı.")

            # Her bir kullanıcı için ayrı bir iş parçacığı oluştur
            client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
            client_thread.start()

if __name__ == "__main__":
    main()
