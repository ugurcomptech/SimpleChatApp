## Simple Chat APP

Bu proje, basit bir soket tabanlı sohbet uygulamasını içerir. Bir sunucu ve bir veya daha fazla istemci arasında mesaj alışverişi yapabilirsiniz.

## Security

Güvenlik kısmı hala geliştirme aşamasındadır. Şuan server tarafında mesajlar encrypt ve decrypt şekilde gözükmekte. İstemci tarafına ise şifre çözülü şekilde geliyor.
**SecureMessageApp** kısmında indirip kullanabilirsiniz, geliştirmeler hala devam etmektedir.


## Chat Odaları

İnsanlar farklı odalarda konuşabilmesi adına yeni bir özellik getirildi bu konuda hala geliştirmeler devam ediyor. 

### Farklı odalar olduğu durumda gördüğünüz gibi mesajlar gözükmüyor.

![image](https://github.com/ugurcomptech/SimpleChatApp/assets/133202238/be8ba83e-6e19-457d-9cca-124493505883)

### Sohbet odaları aynı olduğu durumda bir sorun olmadan mesajlaşılabiliyor.

![image](https://github.com/ugurcomptech/SimpleChatApp/assets/133202238/0a38c96b-ad21-4bbe-a54d-95549faa4221)



## İstemci (Client)

- `client.py` dosyası, istemci tarafını temsil eder.
- Sunucuya bağlanır, kullanıcı adını gönderir ve ardından gelen mesajları dinler.
- Çıkış yapmak için "exit" komutunu kullanabilirsiniz.

## Sunucu (Server)

- `server.py` dosyası, sunucu tarafını temsil eder.
- Kullanıcıları takip eder, gelen mesajları diğer kullanıcılara ileterek bir sohbet odası oluşturur.

## Kullanım

1. `server.py` dosyasını başlatarak sunucuyu başlatın.
2. `client.py` dosyasını başlatarak istemciyi sunucuya bağlayın.
3. Kullanıcı adınızı girin ve sohbetin tadını çıkarın.

## Notlar

- Bu proje hala geliştirme aşamasındadır ve iyileştirmeler içerebilir.
- İletişim hatası durumunda bağlantıyı kontrol etmek önemlidir.

## Katkıda Bulunma

Eğer bu projeye katkıda bulunmak istiyorsanız, lütfen bir çekme isteği (pull request) gönderin veya bir sorun (issue) açın.
