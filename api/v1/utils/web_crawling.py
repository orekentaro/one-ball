import requests

from bs4 import BeautifulSoup


def get_one_table_to_list(url: str, **targets) -> list[list]:
    """指定したURLのHTMLテーブルをリスト形式で取得する"""
    # HTMLを取得
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
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


def get_all_table_to_list(url: str, **targets) -> list[list]:
    """指定したURLのHTMLテーブルを全てリスト形式で取得する"""
    # HTMLを取得
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/115.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")

    tables = soup.find_all("table")

    all_tables_data = []

    # 全テーブルを処理
    for table in tables:
        table_data = []
        for tr in table.find_all("tr"):
            row = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
            if row:
                table_data.append(row)
        all_tables_data.append(table_data)
    return all_tables_data
