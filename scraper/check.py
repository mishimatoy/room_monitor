import requests
from bs4 import BeautifulSoup

# チェック対象ページ
URL = "https://www.ikyu.com/00030497/?adc=1&cbc=1&cid=20260109&discsort=1&lc=1&ppc=1&rc=1&si=1&st=1&top=rooms"

def fetch_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.text

def check_availability(html):
    soup = BeautifulSoup(html, "lxml")

    # 例: “空室” や “円〜” があるか判定
    keywords = ["空室", "円", "残り", "室"]
    hit = any(word in soup.get_text() for word in keywords)

    if hit:
        return "可能性あり：ページ内に空室や料金情報が含まれています"
    else:
        return "検知できず：要 JS レンダリングの可能性あり"

def main():
    html = fetch_html(URL)
    result = check_availability(html)
    print("=== 空室検知結果 ===")
    print(result)

if __name__ == "__main__":
    main()
