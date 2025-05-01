import requests
import string
import time
from itertools import product

# Настройки
domain_zones = ['.com', '.net']  # безопасные зоны
max_length = 3  # длина ключевого слова
protocol = 'http'
delay = 0.1  # задержка между запросами (в секундах)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36"
}

def generate_keywords(max_len):
    characters = string.ascii_lowercase
    for length in range(1, max_len + 1):
        for combo in product(characters, repeat=length):
            yield ''.join(combo)

def check_url(url):
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            print(f"[+] Доступен: {url}")
            return True
    except requests.RequestException as e:
        with open("error_log.txt", "a", encoding="utf-8") as log:
            log.write(f"{url} — ошибка: {e}\n")
    return False

if __name__ == "__main__":
    found = []
    for keyword in generate_keywords(max_length):
        for zone in domain_zones:
            url = f"{protocol}://{keyword}{zone}"
            if check_url(url):
                found.append(url)
            time.sleep(delay)  # пауза между запросами

    print("\n✅ Найденные рабочие сайты:")
    for site in found:
        print(site)
