## Simple Chat APP

Bu proje, basit bir soket tabanlı sohbet uygulamasını içerir. Bir sunucu ve bir veya daha fazla istemci arasında mesaj alışverişi yapabilirsiniz.

## Security

Güvenlik kısmı hala geliştirme aşamasındadır. Şuan server tarafında mesajlar encrypt ve decrypt şekilde gözükmekte. İstemci tarafına ise şifre çözülü şekilde geliyor.
**SecureMessageApp** kısmında indirip kullanabilirsiniz, geliştirmeler hala devam etmektedir.


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
