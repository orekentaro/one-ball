import requests

from bs4 import BeautifulSoup


def get_table_to_list(url: str, **targets) -> list[list]:
    """指定したURLのHTMLテーブルをリスト形式で取得する"""
    # HTMLを取得
    response = requests.get(url)
    response.encoding = response.apparent_encoding  # 日本語ページ対策

    # BeautifulSoupで解析
    soup = BeautifulSoup(response.text, "html.parser")

    # 特定のクラス名やidで<table>を取得する場合
    # 例: get_table_to_list(url, class_="target-class") や get_table_to_list(url, id="target-id")
    table = soup.find("table", **targets)
    # 配列化
    data = []
    for tr in table.find_all("tr"):
        row = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
        if row:  # 空行はスキップ
            data.append(row)
    return data
