from django.utils.translation import gettext_lazy as _


class Constants:
    """定数"""

    TEAM = (
        {
            "id": 3,
            "name": "横浜DeNAベイスターズ",
            "alphabet": "DB",
            "short_name": "DeNA",
            "key": "baystars",
            "league": "C",
        },
        {
            "id": 1,
            "name": "読売ジャイアンツ",
            "alphabet": "G",
            "short_name": "巨人",
            "key": "giants",
            "league": "C",
        },
        {
            "id": 2,
            "name": "東京ヤクルトスワローズ",
            "alphabet": "S",
            "short_name": "ヤクルト",
            "key": "swallows",
            "league": "C",
        },
        {
            "id": 4,
            "name": "中日ドラゴンズ",
            "alphabet": "D",
            "short_name": "中日",
            "key": "dragons",
            "league": "C",
        },
        {
            "id": 6,
            "name": "広島東洋カープ",
            "alphabet": "C",
            "short_name": "広島",
            "key": "carp",
            "league": "C",
        },
        {
            "id": 5,
            "name": "阪神タイガース",
            "alphabet": "T",
            "short_name": "阪神",
            "key": "tigers",
            "league": "C",
        },
        {
            "id": 8,
            "name": "北海道日本ハムファイターズ",
            "alphabet": "F",
            "short_name": "日本ハム",
            "key": "fighters",
            "league": "P",
        },
        {
            "id": 12,
            "name": "福岡ソフトバンクホークス",
            "alphabet": "H",
            "short_name": "ソフトバンク",
            "key": "hawks",
            "league": "P",
        },
        {
            "id": 9,
            "name": "千葉ロッテマリーンズ",
            "alphabet": "M",
            "short_name": "ロッテ",
            "key": "marines",
            "league": "P",
        },
        {
            "id": 11,
            "name": "オリックス・バファローズ",
            "alphabet": "B",
            "short_name": "オリックス",
            "key": "buffaloes",
            "league": "P",
        },
        {
            "id": 376,
            "name": "東北楽天ゴールデンイーグルス",
            "alphabet": "E",
            "short_name": "楽天",
            "key": "eagles",
            "league": "P",
        },
        {
            "id": 7,
            "name": "埼玉西武ライオンズ",
            "alphabet": "L",
            "short_name": "西武",
            "key": "lions",
            "league": "P",
        },
    )

    LEAGUE = (
        ("C", _("セ・リーグ")),
        ("P", _("パ・リーグ")),
    )
