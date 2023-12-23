# server.py
import socket
import threading

# Kullanıcıları ve odaları depolamak için sözlükler
users = {}
rooms = {}

def create_room(room_name):
    """
    Belirli bir isme sahip yeni bir oda oluşturur.
    """
    rooms[room_name] = set()

def join_room(username, room_name):
    """
    Kullanıcıyı belirli bir odaya ekler.
    """
    rooms[room_name].add(username)

def leave_room(username, room_name):
    """
    Kullanıcıyı belirli bir odadan çıkarır.
    """
    rooms[room_name].remove(username)

def decrypt_message(encrypted_message):
    """
    Şifreli mesajı çözer.
    """
    key = 3
    decrypted_message = ''.join([chr((ord(char) - key)) for char in encrypted_message])
    return decrypted_message

def remove_user(username, client_socket):
    """
    Kullanıcıyı sistemden kaldırır.
    """
    if username in users:
        del users[username]
        print(f"{username} bağlantısı kapatıldı.")

def encrypt_message(message):
    """
    Mesajı şifreler.
    """
    key = 3
    encrypted_message = ''.join([chr((ord(char) + key)) for char in message])
    return encrypted_message

def handle_client(client_socket, username, room_name):
    """
    İstemciden gelen mesajları işler.
    """
    try:
        while True:
            encrypted_message = client_socket.recv(1024).decode()
            if not encrypted_message:
                break

            decrypted_message = decrypt_message(encrypted_message)
            print(f"Şifreli Mesaj ({username} - {room_name}): {encrypted_message}")
            print(f"Çözülmüş Mesaj ({username} - {room_name}): {decrypted_message}")

            broadcast_message = f"({username}): {decrypted_message}"
            broadcast_to_room(broadcast_message, room_name, client_socket)
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        remove_user(username, client_socket)
        leave_room(username, room_name)

def broadcast_to_room(message, room_name, sender_socket):
    """
    Belirli bir odadaki tüm kullanıcılara mesajı gönderir.
    """
    if room_name in rooms:
        for user in rooms[room_name]:
            client = users[user]
            if client != sender_socket:
                try:
                    client.send(encrypt_message(message).encode())
                except Exception as e:
                    print(f"Hata (yayın): {e}")

def main():
    """
    Sunucu başlatma ve istemci bağlantılarını kabul etme.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.1.110', 12345))
    server_socket.listen(5)
    print("Sunucu dinleniyor...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Yeni bağlantı: {addr}")

        client_socket.send("Kullanıcı adınızı girin: ".encode())
        username = client_socket.recv(1024).decode()

        # Eğer IP adresi daha önce kaydedilmemişse kullanıcı adını ve oda adını iste ve kaydet
        if username not in users:
            client_socket.send("Oda adınızı girin: ".encode())
            room_name = client_socket.recv(1024).decode()
            
            # Eğer oda daha önce oluşturulmamışsa, yeni bir oda oluştur
            if room_name not in rooms:
                create_room(room_name)

            users[username] = client_socket
            join_room(username, room_name)
            print(f"{username} kullanıcısı {room_name} odasına katıldı.")

            client_thread = threading.Thread(target=handle_client, args=(client_socket, username, room_name))
            client_thread.start()

if __name__ == "__main__":
    main()
