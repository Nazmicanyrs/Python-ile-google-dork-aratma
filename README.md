# 🎯 DorkFinder Pro — Gelişmiş OSINT & Google Dork Arama Motoru

<div align="center">

![GitHub repo size](https://img.shields.io/github/repo-size/Nazmicanyrs/Python-ile-google-dork-aratma?color=cyan&style=for-the-badge)
![License](https://img.shields.io/badge/License-GPL%20%2F%20MIT-blue?style=for-the-badge)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python 3](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)

**Siber güvenlik araştırmacıları, etik korsanlar ve OSINT analistleri için tasarlanmış yüksek performanslı Google Dork ve açık istihbarat aracı.**

[Web Arayüzünü Başlat](#-hızlı-başlangıç) • [Özellikler](#-özellikler) • [GHDB Veritabanı](#-7900-ghdb-arşivi) • [Python Kullanımı](#-python-ile-kullanım) • [Etik Kullanım](#-yasal-ve-etik-uyarı)

</div>

---

## 🌟 Öne Çıkan Özellikler

- 🔍 **7,900+ Exploit-DB GHDB Arşivi**: Resmi OffSec / Exploit-DB Google Hacking Database arşivi yerel olarak entegre edilmiştir. Kategoriye ve anahtar kelimeye göre anlık filtreleme yapılabilir.
- ⚡ **Gelişmiş Dork Üreteci**: Operatörleri (`site:`, `filetype:`, `inurl:`, `intitle:`, `intext:`, `cache:`) tek tıkla birleştirip gerçek zamanlı sözdizimi doğrulaması sunar.
- 🎯 **Hazır Güvenlik Senaryoları (P1 - P4)**:
  - Hassas Kimlik ve Parolalar (`.env`, `wp-config.php`, SSH Private Keys, JWT tokenlar)
  - Açık Dizinler & Log Sızıntıları (`index of /`, `storage/logs`)
  - Veritabanı Yedekleri (`.sql`, `.dump`, `.sqlite`)
  - API ve Bulut Anahtarları (`aws_secret_key`, Google Cloud API Keys)
- 🌐 **9 Farklı Arama & İstihbarat Motoru**:
  - Google, Bing, DuckDuckGo, Yandex, Yahoo, Startpage
  - Shodan, Censys, Wayback Machine (Web Archive)
- 🌓 **Dinamik Karanlık / Aydınlık Mod**: Siber güvenlik operasyonlarına uygun modern karanlık tema ve şık camlaştırma (glassmorphism) efektleri.
- ⌨️ **Klavye Kısayolları**:
  - `Ctrl + K`: Arama çubuğuna odaklan
  - `Ctrl + Shift + C`: Hazırlanan dork sorgusunu panoya kopyala
  - `Alt + T`: Gece / Gündüz temasını değiştir
  - `Esc`: Arama filtresini temizle veya pencereleri kapat
- 📜 **Yerel Arama Geçmişi**: Son yapılan aramaları tarayıcıda saklar ve tek tıkla tekrar kullanmanızı sağlar.
- 🐍 **Python CLI & Sunucu**: Harici hiçbir kütüphaneye ihtiyaç duymadan yerel sunucu açabilir veya terminalden doğrudan arama yapabilir.

---

## 🚀 Hızlı Başlangıç

### 1. Yöntem: Python ile Tek Komutla Çalıştırma (Önerilen)

Depoyu klonlayın ve yerel sunucuyu başlatın:

```bash
git clone https://github.com/Nazmicanyrs/Python-ile-google-dork-aratma.git
cd Python-ile-google-dork-aratma
python dork_search.py
```
> Otomatik olarak varsayılan tarayıcınızda `http://localhost:8000` adresi açılacaktır.

### 2. Yöntem: Doğrudan Tarayıcıda Açma

Herhangi bir kurulum yapmadan doğrudan `index.html` dosyasını tarayıcınızda çift tıklayarak çalıştırabilirsiniz.

---

## 🐍 Python ile Kullanım (CLI & Terminal Modu)

`dork_search.py` aracı hem web sunucusu hem de terminal bazlı bir dork istemcisidir:

#### Terminalde İnteraktif Arama Yapma:
```bash
python dork_search.py --cli
```

#### Doğrudan Belirli Bir Dork Sorgusu Çalıştırma:
```bash
python dork_search.py --dork 'filetype:env "DB_PASSWORD"' --site example.com --engine google
```

#### Farklı Bir Portta Web Sunucusu Başlatma:
```bash
python dork_search.py --port 8080
```

---

## 📚 7,900+ GHDB Arşivi

Bu proje Exploit-DB'nin resmi Google Hacking Database (GHDB) kataloğunu barındırır:
- Toplam **7,900+** kayıt
- 13 farklı güvenlik ve keşif kategorisi
- Yerel IndexedDB önbellekleme desteği
- JSON formatında dışa aktarma (Export) imkanı

---

## 📁 Proje Dosya Yapısı

```
Python-ile-google-dork-aratma/
├── index.html            # Ana web uygulaması ve Dork motoru
├── dork_search.py        # Python CLI ve yerel HTTP sunucusu
├── css/
│   └── index.css         # Modern, duyarlı ve temalı CSS stilleri
├── data/
│   ├── ghdb.js           # 7,900+ kayıtlık GHDB veri kümesi
│   ├── ghdb.xml          # Orijinal Exploit-DB XML arşivi
│   ├── EXPLOITDB-LICENSE.md
│   └── README.md
├── .gitattributes
└── README.md             # Proje dokümantasyonu
```

---

## ⚖️ Yasal ve Etik Uyarı

Bu araç yalnızca **etik siber güvenlik araştırmacıları, penetrasyon testi uzmanları ve sistem yöneticilerinin kendi yetki alanlarındaki sistemlerin güvenlik açıklıklarını tespit etmesi amacıyla** geliştirilmiştir. 

İzin alınmamış sistemler üzerinde yapılan hedefli taramalar ve siber saldırılar yasal suç teşkil edebilir. Geliştirici, aracın kötüye kullanımından sorumlu tutulamaz.

---

## 📄 Lisans

- GHDB verisi Exploit-DB ve OffSec lisans koşullarına tabidir (`data/EXPLOITDB-LICENSE.md`).
- Arayüz ve Python kodları MIT Lisansı altında sunulmaktadır.
