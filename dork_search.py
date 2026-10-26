#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DorkFinder Pro - Python ile Google Dork Aratma & Web Sunucu Aracı
GitHub: https://github.com/Nazmicanyrs/Python-ile-google-dork-aratma
"""

import sys
import os
import argparse
import webbrowser
import urllib.parse
from http.server import SimpleHTTPRequestHandler
import socketserver

PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SEARCH_ENGINES = {
    "google": "https://www.google.com/search?q={}",
    "bing": "https://www.bing.com/search?q={}",
    "duckduckgo": "https://duckduckgo.com/?q={}",
    "yandex": "https://yandex.com/search/?text={}",
    "yahoo": "https://search.yahoo.com/search?p={}",
    "shodan": "https://www.shodan.io/search?query={}",
    "censys": "https://search.censys.io/search?q={}",
    "wayback": "https://web.archive.org/web/*/{}",
}

QUICK_PRESETS = {
    "1": ("Environment (.env) Sızıntıları", 'filetype:env "DB_PASSWORD" OR "DB_HOST" OR "API_KEY"'),
    "2": ("Açık Dizinler (Directory Listing)", 'intitle:"index of /" "parent directory"'),
    "3": ("Veritabanı Yedekleri (.sql, .dump)", 'filetype:sql OR filetype:dump "password" OR "user"'),
    "4": ("Yapılandırma Dosyaları (config.json/yaml)", 'filetype:json OR filetype:yaml "aws_secret_key" OR "secret"'),
    "5": ("SSH & SSL Özel Anahtarları", 'filetype:pem OR filetype:key "BEGIN RSA PRIVATE KEY"'),
    "6": ("Canlı JWT Tokenları", '"eyJhbGciOi" intext:"secret" OR intext:"Bearer" filetype:json OR filetype:log'),
    "7": ("WordPress Hassas Dosyaları", 'inurl:wp-config.php.bak OR inurl:wp-config.bak OR inurl:wp-config.old'),
    "8": ("Yönetici Giriş Panelleri (Admin)", 'inurl:admin OR inurl:login OR inurl:cpanel "login" OR "username"'),
}


def build_search_url(query: str, engine: str = "google", site: str = "") -> str:
    full_query = query.strip()
    if site:
        site_clean = site.replace("https://", "").replace("http://", "").strip("/")
        full_query = f"site:{site_clean} {full_query}"
    
    encoded = urllib.parse.quote(full_query)
    template = SEARCH_ENGINES.get(engine.lower(), SEARCH_ENGINES["google"])
    return template.format(encoded)


def run_server(port: int = PORT, auto_open: bool = True):
    os.chdir(BASE_DIR)
    
    class QuietHandler(SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            # Basit konsol kaydı
            sys.stdout.write(f"[{self.log_date_time_string()}] {format % args}\n")

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), QuietHandler) as httpd:
        url = f"http://localhost:{port}/index.html"
        print("=" * 64)
        print(" 🔥 DorkFinder Pro — Web Arayüzü Başlatıldı")
        print(f" 🌐 Adres: {url}")
        print(" 💡 Durdurmak için Ctrl+C tuşlarına basabilirsiniz.")
        print("=" * 64)
        
        if auto_open:
            webbrowser.open(url)
            
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n Sunucu kapatıldı.")


def interactive_cli():
    print("=" * 64)
    print(" 🎯 DorkFinder Pro — Terminal Arama Modu")
    print("=" * 64)
    target = input("\n[?] Hedef Alan Adı (Örn: example.com, boş bırakılabilir): ").strip()
    
    print("\n[+] Hazır Dork Kategorileri:")
    for key, (title, _) in QUICK_PRESETS.items():
        print(f"  [{key}] {title}")
    print("  [0] Özel Kendi Sorgumu Gireceğim")

    choice = input("\n[?] Seçiminiz (1-8 veya 0) [1]: ").strip() or "1"

    if choice in QUICK_PRESETS:
        title, query = QUICK_PRESETS[choice]
        print(f"\nSeçilen: {title}")
    else:
        query = input("[?] Dork Sorgunuz: ").strip()

    print("\n[+] Arama Motorları:")
    engines = list(SEARCH_ENGINES.keys())
    for i, eng in enumerate(engines, 1):
        print(f"  [{i}] {eng.capitalize()}")
    eng_choice = input(f"\n[?] Motor Seçin (1-{len(engines)}) [1 - Google]: ").strip() or "1"
    
    try:
        engine = engines[int(eng_choice) - 1]
    except (ValueError, IndexError):
        engine = "google"

    url = build_search_url(query=query, engine=engine, site=target)
    print("\n" + "=" * 64)
    print(f" 🔍 Arama Motoru: {engine.capitalize()}")
    print(f" 🚀 Üretilen URL:\n{url}")
    print("=" * 64)
    
    open_browser = input("\n[?] Tarayıcıda açılsın mı? (E/h): ").strip().lower()
    if open_browser in ("", "e", "evet", "y", "yes"):
        webbrowser.open(url)


def main():
    parser = argparse.ArgumentParser(
        description="DorkFinder Pro — Python ile Google Dork Aratma & Yerel Web Sunucusu",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--serve", "-s", action="store_true", help="Web arayüzünü (index.html) yerel HTTP sunucusunda başlat")
    parser.add_argument("--port", "-p", type=int, default=PORT, help=f"Web sunucusu port numarası (varsayılan: {PORT})")
    parser.add_argument("--no-browser", action="store_true", help="Web sunucusu başladığında tarayıcıyı otomatik açma")
    parser.add_argument("--cli", "-c", action="store_true", help="İnteraktif terminal dork arama modunu çalıştır")
    parser.add_argument("--dork", "-d", type=str, help="Doğrudan dork sorgusu çalıştır")
    parser.add_argument("--site", type=str, default="", help="Hedef site filtresi (site:example.com)")
    parser.add_argument("--engine", "-e", type=str, default="google", choices=list(SEARCH_ENGINES.keys()), help="Kullanılacak arama motoru")

    args = parser.parse_args()

    if args.dork:
        url = build_search_url(query=args.dork, engine=args.engine, site=args.site)
        print(f"\n[+] URL: {url}\n")
        webbrowser.open(url)
    elif args.cli:
        interactive_cli()
    else:
        # Varsayılan eylem: Web sunucusunu başlatıp arayüzü aç
        run_server(port=args.port, auto_open=not args.no_browser)


if __name__ == "__main__":
    main()
