from v1.models import Team


def get_grade_url(team: Team, position: str) -> str:
    """
    スポナビの選手成績一覧URLを取得する

    position:
        p: ピッチャー
        b: 野手
    """
    return (
        f"https://baseball.yahoo.co.jp/npb/teams/{team.id}/memberlist?kind={position}"
    )
