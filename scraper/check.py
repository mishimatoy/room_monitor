import requests
from bs4 import BeautifulSoup

# Jina proxy 経由で取得する
URL = "https://r.jina.ai/https://www.ikyu.com/00030497/?adc=1&cbc=1&cid=20260109&discsort=1&lc=1&ppc=1&rc=1&si=1&st=1&top=rooms"

TARGET_WORDS = ["空室", "円", "残り"]

resp = requests.get(URL, timeout=20)
print("HTTP status:", resp.status_code)
text = resp.text

print("=== sample text ===")
print(text[:500])  # 最初の500文字＝動作確認

found = any(word in text for word in TARGET_WORDS)
print("=== 判定結果 ===")
print("FOUND" if found else "NOT FOUND")
